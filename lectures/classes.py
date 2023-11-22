#defined a class but no object yet
class Employee:
    def __init__(self):        #__init__(self) is the constructor. Parameter must be used and be called self 
        self.name =""          #creates attribute called name 
        self.address=""        #MUST assign value to them bc that's how they come into existance in python 
        self.phone=""
        self.department =""
        self.hourlySalary=15.0

    def setName(self, name): #MUST have self as the first argument for every method in class
        self.name = name

    def getName(self):       #has self, but doesn't need any other parameter bc it's a getter
        return(self.name)    #if multiple instances of employees, they all have attribute called name, so self says get the name of THIS object
    
    def aMethodWithALocalVariable(self):
        letsMakeSureWeUnderstandTheDifference = False #not an attribute, local var to this method only
    
    # def someOtherMethod(self):
    #     print(letsMakeSureWeUnderstandTheDifference) #error bc not defined in this method
    
if __name__=="__main__":
    #creating an object of type Employee
    employee1 = Employee()
    #calls the method that sets the name
    employee1.setName("Jenny")    #has 2 arguments but only passes 1 bc "self" gets passed automatically
    #calls the method that reads the name and prints it
    print(employee1.getName())
    
    #2nd object
    employee2 = Employee()
    employee2.setName("Maria")
    print(employee1.getName())  #prints Jenny bc of self keyword