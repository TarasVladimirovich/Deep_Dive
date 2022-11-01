class Person:
    def work(self):
        return 'Person works...'


class Student(Person):
    def work(self):
        result = super().work()
        return f'Student works... and {result}'


s = Student()
print(s.work())


class Person:
    def work(self):
        return 'Person works...'


class Student(Person):
    pass


class PythonStudent(Student):
    def work(self):
        result = super().work()
        return f'PythonStudent codes... and {result}'


ps = PythonStudent()
print(ps.work())


class Person:
    def work(self):
        return f'{self} works...'


class Student(Person):
    def work(self):
        result = super().work()
        return f'{self} studies... and {result}'


class PythonStudent(Student):
    def work(self):
        result = super().work()
        return f'{self} codes... and {result}'


ps = PythonStudent()
print(hex(id(ps)))
print(ps.work())
