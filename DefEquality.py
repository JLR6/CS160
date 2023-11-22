class Person:
    def __init__(self, name = "no name", address= "no address") -> None:
        self.name = name
        self.address = address
    def getName(self):
        return(self.name)
    # def __eq__(self, o):
    #     return(self.getName()==o.getName())
    #^ if not commented out, the new one will override it. In java, won't override bc knows diff of object and str
    def __eq__(self, s):
        newPerson = newPerson(s)
        return(self.getName()==newPerson.getName()) #comparing it w/ string now

p1 = Person("jaime", "amherst")
p2 = Person("maria", "stow")
l = [p1, p2]
l.append(Person("nihkil", "belchertown"))

#^ exactly the same
# l = [Person("jaime", "amherst"), Person("maria", "stow"), Person("nihkil", "belchertown")]
print(p1==p2)
#let's look for an object in the list

for x in l:
    if x=="maria":  #doesn't work bc maria isn't an object. Maria the string doesn't have a getname method. x does
        print("found it!")
    else: 
        print("not here")

#^ violates information hiding and encapsultation (better to just make a class)