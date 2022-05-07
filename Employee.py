class Employee:

    def __init__(self, name, SSN):
        self._name = name
        self._SSN = SSN

    def __hash__(self):
        return hash((self._name, self._SSN))

    @property
    def name(self):
        return self._name

    @property
    def SSN(self):
        return self._SSN

