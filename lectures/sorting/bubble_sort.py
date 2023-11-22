aList = [17, 79, 57, 5]

howManyTimes = 0
while(howManyTimes != len(aList)):
    bubblingHere = 0
    while (bubblingHere != len(aList)-1):
        if aList[bubblingHere] > aList[bubblingHere+1]:
            #swtich elements
            temp = aList[bubblingHere]
            aList[bubblingHere] = aList[bubblingHere+1]
            aList[bubblingHere+1] = temp
            #or can do it this way:
            #aList[bubblingHere], aList[bubblingHere+1] = aList[bubblingHere+1], aList[bubblingHere]
            #^ 3 lines do in one line, not faster bc translated into the same thing in machine code
            #because CPUs can't do more than one thing at a time
        bubblingHere +=1 
    howManyTimes +=1 
print(aList)
#expecting to see [17, 57, 5, 79]