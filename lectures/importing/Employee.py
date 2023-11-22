class Employee: 
    def __init__(self, aName="no name assigned", aDepartment = "no department assigned"):  #runs when object created
        self.name = aName
        self.department = aDepartment
    def getName(self):
        return(self.name)
    def getDepartment(self):
        return(self.department)
    def __str__(self):
        #return("Name:", self.name, "Department:", self.department) wouldn't work bc not ONE string
        return("Name: "  + self.name + " Department: " +  self.department)
    
e2 = Employee("Jenny", "CICS")
if __name__=="__main__":
    e1=Employee() 
    #not a good idea!
    print(e1.getName())         
    print(e1.getDepartment())
    print(e2.getName())         
    print(e2.getDepartment())
    print(e2) #prints location in memory, need string method to print attributes

