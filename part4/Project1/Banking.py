import numbers
import unittest
from collections import namedtuple
from datetime import datetime, timedelta
from itertools import count

from TimeZone import TimeZone

# class TransactionID:
#     def __init__(self, start_id):
#         self._start_id = start_id
#
#     def next(self):
#         self._start_id += 1
#         return self._start_id


# class Account:
#     transaction_counter = TransactionID(100)
#
#     def make_transaction(self):
#         new_trans_id = Account.transaction_counter.next()
#         return new_trans_id
#
#
# def transaction_id(start_id):
#     while True:
#         start_id += 1
#         yield start_id
#
#
# class Account1:
#     transaction_counter = transaction_id(100)
#
#     def make_transaction(self):
#         new_trans_id = next(Account1.transaction_counter)
#         return new_trans_id


Confirmation = namedtuple('Confirmation', 'account_number, transaction_code, transaction_id, time_utc, time')


class Account:
    transaction_counter = count(100)
    _interest_rate = 0.5  # percentage

    _transaction_codes = {
        'deposit': 'D',
        'withdraw': 'W',
        'interest': 'I',
        'rejected': 'X'
    }

    def __init__(self, account_number, first_name, last_name, timezone=None, initial_balance=0):
        # in practice we probably would want to add checks to make sure these values are valid / non-empty
        self._account_number = account_number
        self.first_name = first_name
        self.last_name = last_name

        if timezone is None:
            timezone = TimeZone('UTC', 0, 0)
        self.timezone = timezone

        self._balance = Account.validate_real_number(initial_balance, min_value=0)

    @property
    def account_number(self):
        return self._account_number

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self.validate_and_set_name('_first_name', value, 'First Name')

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self.validate_and_set_name('_last_name', value, 'Last Name')

    # also going to create a full_name computed property, for ease of use
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def timezone(self):
        return self._timezone

    @property
    def balance(self):
        return self._balance

    @timezone.setter
    def timezone(self, value):
        if not isinstance(value, TimeZone):
            raise ValueError('Time zone must be a valid TimeZone object.')
        self._timezone = value

    @classmethod
    def get_interest_rate(cls):
        return cls._interest_rate

    @classmethod
    def set_interest_rate(cls, value):
        if not isinstance(value, numbers.Real):
            raise ValueError('Interest rate must be a real number')
        if value < 0:
            raise ValueError('Interest rate cannot be negative.')
        cls._interest_rate = value

    def validate_and_set_name(self, property_name, value, field_title):
        if value is None or len(str(value).strip()) == 0:
            raise ValueError(f'{field_title} cannot be empty.')
        setattr(self, property_name, value)

    @staticmethod
    def validate_real_number(value, min_value=None):
        if not isinstance(value, numbers.Real):
            raise ValueError('Value must be a real number.')

        if min_value is not None and value < min_value:
            raise ValueError(f'Value must be at least {min_value}')

        # validation passed, return valid value
        return value

    def generate_confirmation_code(self, transaction_code):
        # main difficulty here is to generate the current time in UTC using this formatting:
        # YYYYMMDDHHMMSS
        dt_str = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        return f'{transaction_code}-{self.account_number}-{dt_str}-{next(Account.transaction_counter)}'

    @staticmethod
    def parse_confirmation_code(confirmation_code, preferred_time_zone=None):
        # dummy-A100-20190325224918-101
        parts = confirmation_code.split('-')
        if len(parts) != 4:
            # really simplistic validation here - would need something better
            raise ValueError('Invalid confirmation code')

        # unpack into separate variables
        transaction_code, account_number, raw_dt_utc, transaction_id = parts

        # need to convert raw_dt_utc into a proper datetime object
        try:
            dt_utc = datetime.strptime(raw_dt_utc, '%Y%m%d%H%M%S')
        except ValueError as ex:
            # again, probably need better error handling here
            raise ValueError('Invalid transaction datetime') from ex

        if preferred_time_zone is None:
            preferred_time_zone = TimeZone('UTC', 0, 0)

        if not isinstance(preferred_time_zone, TimeZone):
            raise ValueError('Invalid TimeZone specified.')

        dt_preferred = dt_utc + preferred_time_zone.offset
        dt_preferred_str = f"{dt_preferred.strftime('%Y-%m-%d %H:%M:%S')} ({preferred_time_zone.name})"

        return Confirmation(account_number, transaction_code, transaction_id, dt_utc.isoformat(), dt_preferred_str)

    def deposit(self, value):
        value = Account.validate_real_number(value, min_value=0.01)

        # get transaction code
        transaction_code = Account._transaction_codes['deposit']

        # generate a confirmation code
        conf_code = self.generate_confirmation_code(transaction_code)

        # make deposit and return conf code
        self._balance += value
        return conf_code

    def withdraw(self, value):
        value = Account.validate_real_number(value, min_value=0.01)
        accepted = False
        if self.balance - value < 0:
            # insufficient funds - we'll reject this transaction
            transaction_code = Account._transaction_codes['rejected']
        else:
            transaction_code = Account._transaction_codes['withdraw']
            accepted = True

        conf_code = self.generate_confirmation_code(transaction_code)

        # Doing this here in case there's a problem generating a confirmation code
        # - do not want to modify the balance if we cannot generate a transaction code successfully
        if accepted:
            self._balance -= value

        return conf_code

    def pay_interest(self):
        interest = self.balance * Account.get_interest_rate() / 100
        conf_code = self.generate_confirmation_code(self._transaction_codes['interest'])
        self._balance += interest
        return conf_code


class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account_number = 'A100'
        self.first_name = 'FIRST'
        self.last_name = 'LAST'
        self.tz = TimeZone('TZ', 1, 30)
        self.balance = 100.00

    def create_account(self):
        return Account(self.account_number, self.first_name,
                       self.last_name, self.tz, self.balance)

    def test_create_timezone(self):
        tz = TimeZone('ABC', -1, -30)
        self.assertEqual('ABC', tz.name)
        self.assertEqual(timedelta(hours=-1, minutes=-30), tz.offset)

    def test_timezones_equal(self):
        tz1 = TimeZone('ABC', -1, -30)
        tz2 = TimeZone('ABC', -1, -30)
        self.assertEqual(tz1, tz2)

    def test_timezones_not_equal(self):
        tz = TimeZone('ABC', -1, -30)

        test_timezones = (
            TimeZone('DEF', -1, -30),
            TimeZone('ABC', -1, 0),
            TimeZone('ABC', 1, -30)
        )
        for i, test_tz in enumerate(test_timezones):
            with self.subTest(test_number=i):
                self.assertNotEqual(tz, test_tz)

    def test_create_account(self):
        a = self.create_account()
        self.assertEqual(self.account_number, a.account_number)
        self.assertEqual(self.first_name, a.first_name)
        self.assertEqual(self.last_name, a.last_name)
        self.assertEqual(self.first_name + ' ' + self.last_name, a.full_name)
        self.assertEqual(self.tz, a.timezone)
        self.assertEqual(self.balance, a.balance)

    def test_create_account_blank_first_name(self):
        self.first_name = ""
        with self.assertRaises(ValueError):
            self.create_account()

    def test_create_account_negative_balance(self):
        self.balance = -100.00

        with self.assertRaises(ValueError):
            self.create_account()

    def test_account_deposit_ok(self):
        a = self.create_account()
        conf_code = a.deposit(100)
        self.assertEqual(200, a.balance)
        self.assertIn('D-', conf_code)

    def test_account_deposit_negative_amount(self):
        a = self.create_account()
        with self.assertRaises(ValueError):
            conf_code = a.deposit(-100)

    def test_account_withdraw_ok(self):
        a = self.create_account()
        conf_code = a.withdraw(20)
        self.assertEqual(80, a.balance)
        self.assertIn('W-', conf_code)

    def test_account_withdraw_overdraw(self):
        a = self.create_account()
        conf_code = a.withdraw(200)
        self.assertIn('X-', conf_code)
        self.assertEqual(self.balance, a.balance)


def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)


run_tests(TestAccount)
