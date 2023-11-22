import DefEquality
class People:
    def __init__(self) -> None:
        self.containingList = [] #hiding list inside class
    
    def add(self, p:DefEquality.Person):
        p.getName()
        self.containingList.append(p)

    def search(self, nameImLookingFor:str)->bool:
        for element in self.containingList:
            if element == nameImLookingFor: #remember the __eq__ method we created in DefEquality was based on name
                return(True)
            return(False)
