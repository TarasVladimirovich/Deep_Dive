from datetime import datetime


class TimeUTC:
    def __get__(self, instance, owner_class):
        print(f'__get__ called, self={self}, instance={instance}, owner_class={owner_class}')
        return datetime.utcnow().isoformat()


class Logger1:
    current_time = TimeUTC()


class Logger2:
    current_time = TimeUTC()


# print(Logger1.current_time)
# print(Logger2.current_time)
# l1 = Logger1()
# print(hex(id(l1)))
# l2 = Logger2()
# print(hex(id(l2)))
# print(l2.current_time)


class TimeUTC:
    def __get__(self, instance, owner_class):
        if instance is None:
            # called from class
            return self
        else:
            # called from instance
            return datetime.utcnow().isoformat()


class Logger:
    current_time = TimeUTC()


print(Logger.current_time)
l = Logger()
print(l.current_time)


class Logger:
    @property
    def current_time(self):
        return datetime.utcnow().isoformat()


print(Logger.current_time)
l = Logger()
print(l.current_time)


class Countdown:
    def __init__(self, start):
        self.start = start + 1

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            self.start -= 1
            return self.start


class Rocket:
    countdown = Countdown(10)


rocket1 = Rocket()
rocket2 = Rocket()

print(rocket1.countdown)
print(rocket2.countdown)
print(rocket2.countdown)
print(rocket1.countdown)


class IntegerValue:
    def __set__(self, instance, value):
        print(f'__set__ called, instance={instance}, value={value}')

    def __get__(self, instance, owner_class):
        if instance is None:
            print('__get__ called from class')
        else:
            print(f'__get__ called, instance={instance}, owner_class={owner_class}')


class Point2D:
    x = IntegerValue()
    y = IntegerValue()


# Point2D.x
# p = Point2D()
# p.x
# p.x = 100
# print(p.x)


class IntegerValue:
    def __set__(self, instance, value):
        self._value = int(value)

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return self._value


class Point2D:
    x = IntegerValue()
    y = IntegerValue()


p1 = Point2D()
p1.x = 1.1
p1.y = 2.2
print(p1.x, p1.y)
p2 = Point2D()
print(p2.x, p2.y)
p2.x = 100.9
print(p2.x, p1.x)
