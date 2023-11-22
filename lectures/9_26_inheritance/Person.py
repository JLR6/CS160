class Person:
    def __init__(self, aName ="none assigned"):
        self.name = aName

    
    def getName(self):
        return("Name: " + self.name)
    

    def setName(self, newName):
        self.name = newName

    def __str__(self):
        return(self.name)

if __name__=="__main__":
    p1 = Person("Jenny")
    print(p1.getName())
    print(p1)