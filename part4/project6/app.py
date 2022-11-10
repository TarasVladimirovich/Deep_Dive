import traceback
import json
from datetime import datetime
from http import HTTPStatus


class WidgetException(Exception):
    message = 'Generic Widget exception.'
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR

    def __init__(self, *args, customer_message=None):
        super().__init__(*args)
        if args:
            self.message = args[0]
        self.customer_message = customer_message if customer_message is not None else self.message

    @property
    def traceback(self):
        return traceback.TracebackException.from_exception(self).format()

    def log_exception(self):
        exception = {
            "type": type(self).__name__,
            "message": self.message,
            "args": self.args[1:],
            "traceback": list(self.traceback)
        }
        print(f'EXCEPTION: {datetime.utcnow().isoformat()}: {exception}')

    def to_json(self):
        response = {
            'code': self.http_status.value,
            'message': '{}: {}'.format(self.http_status.phrase, self.customer_message),
            'category': type(self).__name__,
            'time_utc': datetime.utcnow().isoformat()
        }
        return json.dumps(response)


class SupplierException(WidgetException):
    message = 'Supplier exception.'
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR


class NotManufacturedException(SupplierException):
    message = 'Widget is no longer manufactured by supplier.'
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR


class ProductionDelayedException(SupplierException):
    message = 'Widget production has been delayed by supplier.'
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR


class ShippingDelayedException(SupplierException):
    message = 'Widget shipping has been delayed by supplier.'
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR


class CheckoutException(WidgetException):
    message = 'Checkout exception.'
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR


class InventoryException(CheckoutException):
    message = 'Checkout inventory exception.'
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR


class OutOfStockException(InventoryException):
    message = 'Inventory out of stock'
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR


class PricingException(CheckoutException):
    message = 'Checkout pricing exception.'
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR


class InvalidCouponCodeException(PricingException):
    message = 'Invalid checkout coupon code.'
    http_status = HTTPStatus.BAD_REQUEST


class CannotStackCouponException(PricingException):
    message = 'Cannot stack checkout coupon codes.'
    http_status = HTTPStatus.BAD_REQUEST


# try:
#     raise CannotStackCouponException()
# except WidgetException as ex:
#     ex.log_exception()
#     raise


ex1 = WidgetException('some custom message', 10, 100)
ex2 = WidgetException(customer_message='A custom user message.')

ex1.log_exception()
ex2.log_exception()
e = WidgetException('same custom message for log and user')
print("=Json=" * 10)
print(json.loads(e.to_json()))
print(e.to_json())
print("*" * 25)
print(ex1.args)
print(ex2.args)

print("*" * 25)
try:
    raise WidgetException('custom error message')
except WidgetException as ex:
    print(repr(ex.__traceback__))
    print(list(ex.traceback))

print("*" * 25)
try:
    raise ValueError
except ValueError:
    try:
        raise WidgetException('custom error message')
    except WidgetException as ex:
        print(list(traceback.TracebackException.from_exception(ex).format()))
        print(''.join(ex.traceback))

print("*" * 25)
print("*" * 25)
print("*" * 25)
try:
    raise ValueError
except ValueError:
    try:
        raise InvalidCouponCodeException(
            'User tried to use an old coupon', customer_message='Sorry. This coupon has expired.'
        )
    except InvalidCouponCodeException as ex:
        ex.log_exception()
        print('------------')
        print(ex.to_json())
        print('------------')
        print(''.join(ex.traceback))
