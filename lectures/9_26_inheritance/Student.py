import Person
class Student(Person.Person):
    def __init__(self, name = "none assigned", major = "none delcared"):
        super().__init__(name)
        self.major = major
    