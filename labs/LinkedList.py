import Person

#reflector - Jenny
#laison - hayun 
#synchronizer - Eric 
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
            current_last.setNext(newNode)
            newNode.setPrevious(current_last)
            self.tail = newNode
        self.size = self.size + 1

    def bubble_once(self):
        bubbleUpToHere = self.size
        bubblingHere = 0
        curr = self.head
        while (bubblingHere < bubbleUpToHere-1): 
            if curr.getData() > curr.getNext().getData():
                #swtich elements
                temp = curr.getData()
                curr.setData(curr.getNext().getData())
                curr.getNext().setData(temp)
            curr=curr.getNext()
            bubblingHere +=1     

    def bubble_once_optimzed(self, bubbleUpToHere):
        bubblingHere = 0
        curr = self.head
        while (bubblingHere != bubbleUpToHere): 
            if curr.getData() > curr.getNext().getData():
                #swtich elements
                temp = curr.getData()
                curr.setData(curr.getNext().getData())
                curr.getNext().setData(temp)
            curr=curr.getNext()
            bubblingHere +=1 
    
    def bubble(self):
        howManyTimes = 0
        while(howManyTimes != self.size):
            self.bubble_once()
            howManyTimes +=1  

    def bubble_optimized(self):
        howManyTimes = 0
        while(howManyTimes != self.size):
            self.bubble_once_optimzed(self.size-1-howManyTimes)
            howManyTimes +=1   

    def __str__(self):
        stringToReturn = "List size: " + str(self.size)
        current = self.head
        # don't do this
        # while (current != None)
        # while (current)
        while (current is not None):
        # like saying while (not(current is None))    
            stringToReturn = stringToReturn + "\n\n" + str(current)
            current = current.getNext()
        return(stringToReturn)

if __name__ == "__main__":
    aList = LinkedList()
    #one with 1 number
    # aList.add(2)
    # aList.bubble()
    # print(aList)

    #one with 2 of the same number
    # aList.add(5)
    # aList.add(2)
    # aList.add(7)
    # aList.add(2)
    # aList.bubble()
    # print(aList)

    #one with all the same number
    # aList.add(5)
    # aList.add(5)
    # aList.add(5)
    # aList.bubble()
    # print(aList)

    #one already in order
    # aList.add(2)
    # aList.add(5)
    # aList.add(7)
    # aList.bubble()
    # print(aList)

    #one in decending order
    # aList.add(7)
    # aList.add(5)
    # aList.add(2)
    # aList.bubble()
    # print(aList)

    #empty linked list
    # aList.bubble()
    # print(aList)

    # aList.add(17)
    # aList.add(79)
    # aList.add(57)
    # aList.add(5)
    # aList.bubble_optimized()
    # print(aList)
    # print(aList)
    # aList.bubble()
    # print(aList)
    #excepting 17, 57, 5, 79
    # aList.bubble()
    # print(aList)
    #excpecting 5, 17, 57, 79
    # aList.bubble_optimized()
    # print(aList)

    #compare strings
    # aList.add("apple")
    # aList.add("cat")
    # aList.add("banana")
    # aList.add("goat")
    # aList.bubble_optimized()
    # aList.bubble()
    # print(aList)
    # aList.add("Apple")
    # aList.add("apple")
    # aList.add("Banana")
    # aList.add("Goat")
    # aList.add("cat")
    # aList.bubble()
    # aList.bubble_optimized()
    # print(aList)

    #testing objects
    # aList.add(Person.Person("Jenny"))
    # aList.add(Person.Person("Eric"))
    # aList.add(Person.Person("Hayun"))
    # aList.bubble()
    # print(aList)
