import Person

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, e):
        if self.size == 0:
            self.head = e
            self.tail = e
        else:
            current_last = self.tail
            current_last.setNext(e)
            e.setPrevious(current_last)
            self.tail = e
        self.size = self.size + 1

    def delete(self, i):
        if self.size ==1:
            self.head = None
            self.tail = None
            self.size-=1
        else:
            if i==0:
                second = self.head.getNext()
                third = second.getNext()
                self.head = second
                second.setPrevious(None) 
                self.head.setNext(third)
                self.size-=1
            elif i==self.size-1:
                
                current = self.tail
                self.tail = current.getPrevious()
                current.setPrevious(None)
                self.tail.setNext(None)
                self.size-=1
                
                
            else:
                current = self.head
                counter = 0
                while counter < i:
                    current = current.getNext()
                    counter +=1
                
                current.getNext().setPrevious(current.getPrevious())
                current.getPrevious().setNext(current.getNext())
                current.setPrevious(None)
                current.setNext(None)
                self.size-=1
            

    def __str__(self):
        stringToReturn = "List size: " + str(self.size)
        current = self.head
        while (current is not None):
            stringToReturn = stringToReturn + "\n\n" + str(current)
            current = current.getNext()
        return(stringToReturn)

if __name__ == "__main__":
    listOfPeople = LinkedList()
    listOfPeople.add(Person.Person("Jaime", "Amherst"))
    listOfPeople.add(Person.Person("Maria", "Stow"))
    listOfPeople.add(Person.Person("Maria", "Malden"))
    listOfPeople.add(Person.Person("Jenny", "Amherst"))
    print(listOfPeople)
    # print("Now testing:")
    # listOfPeople.delete(2)
    # print(listOfPeople)
    # print("Now testing:")
    # listOfPeople.delete(0)
    # print(listOfPeople)
    # print("Now testing:")
    # listOfPeople.delete(3)
    # print(listOfPeople)
    print("Now testing:")
    listOfPeople.delete(1)
    print(listOfPeople)
    
