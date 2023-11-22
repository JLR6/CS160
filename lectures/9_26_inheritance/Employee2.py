import Person
class Employee(Person.Person):
    def __init__(self, name="none assigned", salary=15):
        super().__init__(name)
        self.salary = salary
    # def getName(self):
    #     return(self.name)
    def setSalary(self, newSalary):
        if(newSalary >= 15):
            self.salary=newSalary

    # def __str__(self):
    #     return(super().__str__() + " " + str(self.salary))

if __name__=="__main__":
    e1 = Employee()
    print(e1)