import enum


class NumSides(enum.Enum):
    Triangle = 3
    Rectangle = 4
    Square = 4
    Rhombus = 4


print(list(NumSides))
print(NumSides.__members__)
print(NumSides.Rectangle is NumSides.Square)
print(NumSides.Square is NumSides.Rhombus)
print(NumSides.Square in NumSides)
print(NumSides(4))
print(NumSides['Square'])


class Status(enum.Enum):
    ready = 'ready'

    running = 'running'
    busy = 'running'
    processing = 'running'

    ok = 'ok'
    finished_no_error = 'ok'
    ran_ok = 'ok'

    errors = 'errors'
    finished_with_errors = 'errors'
    errored = 'errors'


print(list(Status))
print(Status['busy'])


class Status(enum.Enum):
    ready = 1

    running = 2
    busy = 2
    processing = 2

    ok = 3
    finished_no_error = 3
    ran_ok = 3

    errors = 4
    finished_with_errors = 4
    errored = 4


print(Status.ran_ok)
status = 'ran_ok'
print(status in Status.__members__)


@enum.unique
class Status(enum.Enum):
    ready = 1
    done_ok = 2
    errors = 3


try:
    @enum.unique
    class Status(enum.Enum):
        ready = 1
        waiting = 1
        done_ok = 2
        errors = 3
except ValueError as ex:
    print(ex)
