import Person1
from Node import Node
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, e):
        newNode = Node(e)
        if self.size == 0:
            self.head = newNode
            self.tail = newNode
        else:
            current_last = self.tail
            current_last.setNext(newNode) #can't do this bc Person doesn't have next attribute 
            newNode.setPrevious(current_last)
            self.tail = newNode
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
            
    def __getitem__(self, i):
        currentElement = self.head
        howManyHaveISkipped = 0
        while(howManyHaveISkipped < i):
            currentElement = currentElement.getNext()
            howManyHaveISkipped +=1
        return(currentElement.getData()) #this works when Node doesn't have __str__
            
    def __str__(self):
        stringToReturn = "List size: " + str(self.size)
        current = self.head  
        while (current is not None): #can't do current!= None bc current is a pointer, not a boolean expression, can't evaluate to true/false
            stringToReturn = stringToReturn + "\n\n" + str(current) #None is an object type
            current = current.getNext()
        return(stringToReturn)
    def __setitem__(self, i, v):
        current = self.head
        howManyIHaveSkippedOver = 0
        while (howManyIHaveSkippedOver < i):
            current = current.getNext()
            howManyIHaveSkippedOver +=1
        current.setData(v)
    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.getData()
            current = current.getNext()
    def mergesort(self):
        if(self.size<2):
            return (self) #returning the list
        else:
            # self.split(0, self.size//2)
            # self.split(self.size//2, self.size)
            a = self[0, self.size//2]
            b = self[self.size//2, self.size-1]
            a.mergesort()
            b.mergesort()
            return(a.merge(b))

    def merge(self, theOtherList):
        pass
if __name__ == "__main__":
    # listOfPeople = LinkedList()
    # listOfPeople.add(Person1.Person1("Jaime"))
    # listOfPeople.add(Person1.Person1("Maria"))
    # listOfPeople.add(Person1.Person1("Maria"))
    # listOfPeople.add(Person1.Person1("Jenny"))
    # print(listOfPeople)
    # print("Now testing:")
    # listOfPeople.delete(2)
    # print(listOfPeople)
    # print("Now testing:")
    # listOfPeople.delete(0)
    # print(listOfPeople)
    # print("Now testing:")
    # listOfPeople.delete(3)
    # print(listOfPeople)
    # print("Now testing:")
    # listOfPeople.delete(1)
    # print(listOfPeople)
    l = LinkedList()
    l.add(42)
    l.add(17)
    l.add(19)
    l[1] = 99
    print(l[1])
    # l2 = ["a", "b"]
    # print(l2[10])
    for e in l:
        print(e)