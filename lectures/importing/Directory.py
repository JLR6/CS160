import importing.Employee as Employee
# directoryOfEmployees =[]
# e = Employee.Employee("Maria", "python team")  #telling it to find Class employee in module Employee, prefers this
# directoryOfEmployees.append(e)
# directoryOfEmployees.append(Employee.Employee("a second person", "a second department"))
# print(directoryOfEmployees)   #prints location, if was class can use dunder method to achieve same thing as for loop to print instead of printing memroy
# # print(directoryOfEmployees[0]) #prints attributes
# # print(directoryOfEmployees[1])

# for emp in directoryOfEmployees:  #uses __str__ method to print objects
#     print(emp)

class Directory:
    def __init__(self):
        self.aList = []
    def add(self, smthToAdd):
        self.aList.append(smthToAdd)
    def __str__(self):
        stringToReturn = ""
        for elem in self.aList:
            stringToReturn = stringToReturn + str(elem) + "\n" #calls elem's __str__ method in class Employee 
        return stringToReturn

if __name__ == "__main__":
    d = Directory()
    d.add(Employee.Employee("Nikhil", "Management"))
    d.add(Employee.Employee("Jane", "HR"))
    print(d)    



# print(Employee.e2)    #if want to use an object in main class, the object must be defined in main class outside of if __name__ block and must directly define e2 here with Employee.e2



# import Employee
# directoryOfEmployees =[]
# e = Employee("Maria", "python team")  #e is a module (the file) which is not callable, we want to call object not module
# directoryOfEmployees.append(e)



# import Employee
# from Employee import Employee  #telling it to find class employee in module employee
# directoryOfEmployees =[]
# e = Employee.Employee("Maria", "python team")  #telling it to find Class employee in module Employee 
# directoryOfEmployees.append(e)