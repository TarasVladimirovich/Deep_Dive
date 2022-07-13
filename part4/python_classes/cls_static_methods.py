class Person:
    def hello(arg='default'):
        print(f'Hello, with arg={arg}')


# Person.hello()
# p = Person()
# p.hello()


class MyClass:
    def hello():
        print('hello...')

    def instance_hello(arg):
        print(f'hello from {arg}')

    @classmethod
    def class_hello(arg):
        print(f'hello from {arg}')

    @staticmethod
    def static_hello():
        print('Static method not bound to anything')


m = MyClass()
MyClass.hello()
# m.hello() ERROR
try:
    m.hello()
except TypeError as ex:
    print(ex)
m.instance_hello()
m.class_hello()
MyClass().class_hello()
MyClass.class_hello()
MyClass.static_hello()
m.static_hello()

from datetime import datetime, timezone, timedelta


class TimerError(Exception):
    """A custom exception used for Timer class"""
    # (since """...""" is a statement, we don't need to pass)


class Timer:
    tz = timezone.utc  # class variable to store the timezone - default to UTC

    def __init__(self):
        # use these instance variables to keep track of start/end times
        self._time_start = None
        self._time_end = None

    @staticmethod
    def current_dt_utc():
        """Returns non-naive current UTC"""
        return datetime.now(timezone.utc)

    @classmethod
    def set_tz(cls, offset, name):
        cls.tz = timezone(timedelta(hours=offset), name)

    @classmethod
    def current_dt(cls):
        return datetime.now(cls.tz)

    def start(self):
        # internally we always non-naive UTC
        self._time_start = self.current_dt_utc()
        self._time_end = None

    def stop(self):
        if self._time_start is None:
            # cannot stop if timer was not started!
            raise TimerError('Timer must be started before it can be stopped.')
        self._time_end = self.current_dt_utc()

    @property
    def start_time(self):
        if self._time_start is None:
            raise TimerError('Timer has not been started.')
        # since tz is a class variable, we can just as easily access it from self
        return self._time_start.astimezone(self.tz)

    @property
    def end_time(self):
        if self._time_end is None:
            raise TimerError('Timer has not been stopped.')
        return self._time_end.astimezone(self.tz)

    @property
    def elapsed(self):
        if self._time_start is None:
            raise TimerError(
                'Timer must be started before an elapsed time is available')

        if self._time_end is None:
            # timer has not ben stopped, calculate elapsed between start and now
            elapsed_time = self.current_dt_utc() - self._time_start
        else:
            # timer has been stopped, calculate elapsed between start and end
            elapsed_time = self._time_end - self._time_start

        return elapsed_time.total_seconds()


Timer.set_tz(-7, 'MST')
print(Timer.tz)
print(Timer.current_dt_utc())
print(Timer.current_dt_utc(), Timer.current_dt())
