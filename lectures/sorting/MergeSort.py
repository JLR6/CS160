
def mergeSort(aList):
    if (len(aList) < 2):
        return(aList)
    else:
        a = aList[0:len(aList)//2] #int divison
        b = aList[len(aList)//2: len(aList)] #remember that the last one is exclusive
        aButSorted = mergeSort(a)
        bButSorted = mergeSort(b)
        # "somehow combine them"
        return(merge(aButSorted, bButSorted))
def merge(listA, listB):
    newList = []
    while(len(listA)>0 and len(listB)> 0):
        if(listA[0]<listB[0]):
            newList.append(listA[0])
            listA.pop(0)  #gets rid of this elemment, pop has complexity O(n) so this whole thing is O(n^2)
            #better way:
            #hereInA = hereInA+1
        else:
            newList.append(listB[0])
            listB.pop(0)
    #at this point one of the lists is empty but we don't know which one,
    #so append from both using extend() - this appends multiple elements
    newList.extend(listA)
    newList.extend(listB)
    return(newList)

if __name__ == "__main__":
    #OOPS! this doesn't work.
    # extend returns nothing!
    # print([7,22,9].extend([99,-1]))
    # original = [7,22,9]
    # original.extend([])
    # print(original)
    aList = [42, -1, 0 , 17, 23, 37, -7]
    # mergesort DOES return a new list.
    newList = mergeSort(aList)
    print(newList)

    #print([7,22,9].extend([99, -1])) #extend returns nothing so these don't work either:
    # printThis = [7,22,9].extend([99, -1])
    # print(printThis)
    # original = [7, 22, 9]
    # original.extend([99, -1])
    # print(original)



