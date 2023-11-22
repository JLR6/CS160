aList = [17, 79, 57, 5]

#old bubble_once-------------------------------
# def bubble_once(aList):
#     bubblingHere = 0
#     while (bubblingHere != len(aList)-1):
#         if aList[bubblingHere] > aList[bubblingHere+1]:
#             #swtich elements
#             temp = aList[bubblingHere]
#             aList[bubblingHere] = aList[bubblingHere+1]
#             aList[bubblingHere+1] = temp
#         bubblingHere +=1 

def bubble_once(aList, bubbleUpToHere):
    bubblingHere = 0
    while (bubblingHere != bubbleUpToHere-1): 
        if aList[bubblingHere] > aList[bubblingHere+1]:
            #swtich elements
            temp = aList[bubblingHere]
            aList[bubblingHere] = aList[bubblingHere+1]
            aList[bubblingHere+1] = temp
        bubblingHere +=1 
        #we just compared bubblingHere with bubblingHere+1
 

def bubbleTheWholeThing(myList):
    howManyTimes = 0
    while(howManyTimes != len(myList)):
        bubble_once(myList, len(myList-1-howManyTimes))
        howManyTimes +=1 
print(aList)
