#pop has complexity O(n) because when removing, python has to move everything
# down in memory which iterates through the whole list

def mergeSort(aList):
    if (len(aList) < 2):
        return(aList)
    else:
        a = aList[0:len(aList)//2] #int divison
        b = aList[len(aList)//2: len(aList)] #remember that the last one is exclusive
        aButSorted = mergeSort(a)
        bButSorted = mergeSort(b)
        return(merge(aButSorted, bButSorted))

def merge(listA, listB):
    newList = []
    newIndexA = 0
    newIndexB =0
    #as long as the new indexes are within range (less than length, and >=0, since they can never be negative)
    while (newIndexA < len(listA)) and (newIndexB < len(listB)):
        #if an element of listA is bigger, add from listB
        if listA[newIndexA] > listB[newIndexB]:
            newList.append(listB[newIndexB])
            #add 1 to new element to avoid using pop
            newIndexB += 1
        #same thing but add from listA
        else:
            newList.append(listA[newIndexA])
            #add 1 to new element to avoid using pop
            newIndexA += 1
    #the while loop won't go through the whole list, so use slicing to get the last elements left
    newList += listA[newIndexA:]
    newList += listB[newIndexB:]

    return(newList)


if __name__ == "__main__":
    #testing empty list

    firstList = []
    newList = mergeSort(firstList)
    print(newList)

    #testing list with negative numbers

    secondList = [5, -7, 8, -1]
    newBList = mergeSort(secondList)
    print(newBList)

    #testing list with repeating numbers

    thirdList = [9, 6, 9, 3]
    newCList = mergeSort(thirdList)
    print(newCList)

    #testing list with one number

    fourthList = [5]
    newDList = mergeSort(fourthList)
    print(fourthList)

    #testing list with 0

    fifthList = [3,6,7,0]
    newEList = mergeSort(fifthList)
    print(newEList)

    #testing list with odd number of elements

    sixthList = [4,2,6,9,1]
    newFList = mergeSort(sixthList)
    print(newFList)

    #testing empty with non-empty

    sevList = []
    eigList =[5, 1]
    newGList = merge(sevList, eigList)
    print(newGList)

    #testing non-empty

    ninList =[1,6]
    tenList=[4, 5, 8]
    newHList = merge(ninList, tenList)
    print(newHList)

