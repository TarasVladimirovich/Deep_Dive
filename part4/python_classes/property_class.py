class Person:
    """ Single Person """

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        """ Getter """
        return self._name

    @name.setter
    def name(self, name):
        """ Setter """
        self._name = name

    @name.deleter
    def name(self):
        del self._name


print(help(Person))
