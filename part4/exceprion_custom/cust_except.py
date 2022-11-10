import sys
import json
from http import HTTPStatus
from datetime import datetime


class TimeOutError(Exception):
    """Timeout exception"""


try:
    raise TimeOutError('timeout occurred')
except TimeOutError:
    ex_type, ex, tb, = sys.exc_info()
    print(ex_type, ex, tb)

"""
WebScraperException
   - HTTPException
       - InvalidUrlException
       - TimeoutException
           - PingTimeoutException
           - LoadTimeoutException
    - ParserException
"""


class WebScraperException(Exception):
    """Base exception for WebScraper"""


class HTTPException(WebScraperException):
    """General HTTP exception for WebScraper"""


class InvalidUrlException(HTTPException):
    """Indicates the url is invalid (dns lookup fails)"""


class TimeoutException(HTTPException):
    """Indicates a general timeout exception in http connectivity"""


class PingTimeoutException(TimeoutException):
    """Ping time out"""


class LoadTimeoutException(TimeoutException):
    """Page load time out"""


class ParserException(WebScraperException):
    """General page parsing exception"""


try:
    raise PingTimeoutException('Ping time out')
except WebScraperException as ex:
    print(repr(ex))
    print(ex)

"""
APIException
   - ApplicationException (5xx errors)
       - DBException
           - DBConnectionError
   - ClientException
       - NotFoundError
       - NotAuthorizedError
"""


class APIException(Exception):
    """Base API exception"""


class ApplicationException(APIException):
    """Indicates an application error (not user caused) - 5xx HTTP type errors"""


class DBException(ApplicationException):
    """General database exception"""


class DBConnectionError(DBException):
    """Indicates an error connecting to database"""


class ClientException(APIException):
    """Indicates exception that was caused by user, not an internal error"""


class NotFoundError(ClientException):
    """Indicates resource was not found"""


class NotAuthorizedError(ClientException):
    """User is not authorized to perform requested action on resource"""


class Account:
    def __init__(self, account_id, account_type):
        self.account_id = account_id
        self.account_type = account_type


def lookup_account_by_id(account_id):
    # mock of various exceptions that could be raised getting an account from database
    if not isinstance(account_id, int) or account_id <= 0:
        raise ClientException(f'Account number {account_id} is invalid.')

    if account_id < 100:
        raise DBConnectionError('Permanent failure connecting to database.')
    elif account_id < 200:
        raise NotAuthorizedError('User does not have permissions to read this account')
    elif account_id < 300:
        raise NotFoundError(f'Account not found.')
    else:
        return Account(account_id, 'Savings')


def get_account(account_id):
    try:
        account = lookup_account_by_id(account_id)
    except ApplicationException as ex:
        return HTTPStatus.INTERNAL_SERVER_ERROR, str(ex)
    except NotFoundError as ex:
        return HTTPStatus.NOT_FOUND, 'The account {} does not exist.'.format(account_id)
    except NotAuthorizedError as ex:
        return HTTPStatus.UNAUTHORIZED, 'You do not have the proper authorization.'
    except ClientException as ex:
        return HTTPStatus.BAD_REQUEST, str(ex)
    else:
        return HTTPStatus.OK, {"id": account.account_id, "type": account.account_type}


print(get_account(550))


class APIException(Exception):
    """Base API exception"""

    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = 'API exception occurred.'
    user_err_msg = "We are sorry. An unexpected error occurred on our end."

    def __init__(self, *args, user_err_msg=None):
        if args:
            self.internal_err_msg = args[0]
            super().__init__(*args)
        else:
            super().__init__(self.internal_err_msg)

        if user_err_msg is not None:
            self.user_err_msg = user_err_msg

    def to_json(self):
        err_object = {'status': self.http_status, 'message': self.user_err_msg}
        return json.dumps(err_object)

    def log_exception(self):
        exception = {
            "type": type(self).__name__,
            "http_status": self.http_status,
            "message": self.args[0] if self.args else self.internal_err_msg,
            "args": self.args[1:]
        }
        print(f'EXCEPTION: {datetime.utcnow().isoformat()}: {exception}')


print("==" * 18)
try:
    raise APIException('custom message...', 10, 20, user_err_msg="qwerty")
except APIException as ex:
    print(repr(ex))
    print(ex.user_err_msg)
    print(ex.internal_err_msg)
    print(ex.http_status)
print("==" * 18)
try:
    raise APIException()
except APIException as ex:
    print(repr(ex), ex.to_json())
print("==" * 18)
try:
    raise APIException()
except APIException as ex:
    ex.log_exception()
    print(ex.to_json())


class ApplicationException(APIException):
    """Indicates an application error (not user caused) - 5xx HTTP type errors"""
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = "Generic server side exception."
    user_err_msg = "We are sorry. An unexpected error occurred on our end."


class DBException(ApplicationException):
    """General database exception"""
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = "Database exception."
    user_err_msg = "We are sorry. An unexpected error occurred on our end."


class DBConnectionError(DBException):
    """Indicates an error connecting to database"""
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = "DB connection error."
    user_err_msg = "We are sorry. An unexpected error occurred on our end."


class ClientException(APIException):
    """Indicates exception that was caused by user, not an internal error"""
    http_status = HTTPStatus.BAD_REQUEST
    internal_err_msg = "Client submitted bad request."
    user_err_msg = "A bad request was received."


class NotFoundError(ClientException):
    """Indicates resource was not found"""
    http_status = HTTPStatus.NOT_FOUND
    internal_err_msg = "Resource was not found."
    user_err_msg = "Requested resource was not found."


class NotAuthorizedError(ClientException):
    """User is not authorized to perform requested action on resource"""
    http_status = HTTPStatus.UNAUTHORIZED
    internal_err_msg = "Client not authorized to perform operation."
    user_err_msg = "You are not authorized to perform this request."


def lookup_account_by_id(account_id):
    # mock of various exceptions that could be raised getting an account from database
    if not isinstance(account_id, int) or account_id <= 0:
        raise ClientException(f'Account number {account_id} is invalid.',
                              f'account_id = {account_id}',
                              'type error - account number not an integer')

    if account_id < 100:
        raise DBConnectionError('Permanent failure connecting to database.', 'db=db01')
    elif account_id < 200:
        raise NotAuthorizedError('User does not have permissions to read this account', f'account_id={account_id}')
    elif account_id < 300:
        raise NotFoundError(f'Account not found.', f'account_id={account_id}')
    else:
        return Account(account_id, 'Savings')


def get_account(account_id):
    try:
        account = lookup_account_by_id(account_id)
    except APIException as ex:
        ex.log_exception()
        return ex.to_json()
    else:
        return HTTPStatus.OK, {"id": account.account_id, "type": account.account_type}


print("!@#" * 20)
print(get_account('ABC'))
get_account('ABC')


#### Inheriting from Multiple Exceptions

class AppException(Exception):
    """generic application exception"""


class NegativeIntegerError(AppException, ValueError):
    """Used to indicate an error when an integer is negative."""


def set_age(age):
    if age < 0:
        raise NegativeIntegerError('age cannot be negative')


print("\n"*2)
try:
    set_age(-10)
except ValueError as ex:
    print(repr(ex))

try:
    set_age(-10)
except NegativeIntegerError as ex:
    print(repr(ex))
