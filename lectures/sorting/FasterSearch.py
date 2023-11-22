lint = []
lint.append(2)
lint.append(3)
lint.append(5)
lint.append(7)
lint.append(7)
lint.append(7)
lint.append(7)
lint.append(7)
lint.append(7)
lint.append(7)
lint.append(7)
lint.append(7)
lint.append(7)
lint.append(7)
lint.append(7)
lint.append(7)
lint.append(7)
lint.append(7)
lint.append(7)
lint.append(7)
lint.append(7)
lint.append(7)
lint.append(7)
lint.append(7)
lint.append(7)
lint.append(7)
lint.append(7)
lint.append(7)
lint.append(7)
lint.append(7)
lint.append(7)
lint.append(7)
lint.append(7)
lint.append(7)
lint.append(11)
lint.append(13)
whatWereLookingFor = -7
print(lint)
#beginning and end
smallestPossible = 0
biggestPossible = len(lint) -1
#finding the average
letslookhere = (smallestPossible+biggestPossible)//2 #int division
print("the middle point is", letslookhere)
print("the element right at the middle is", lint[letslookhere]) #can't do this w/float
found = False
howManyTimesWeHaveLooked = 0
while (smallestPossible <= biggestPossible and not found):
    howManyTimesWeHaveLooked = howManyTimesWeHaveLooked+1
    print("will compare", whatWereLookingFor ,"with",lint[letslookhere])
    if lint[letslookhere] == whatWereLookingFor:
        print("FOUND IT!")
        found = True
    else:
        print("not yet")
        if lint[letslookhere] > whatWereLookingFor:
            biggestPossible = letslookhere - 1
        else:
            smallestPossible = letslookhere+1
        letslookhere = (smallestPossible+biggestPossible)//2
# RIGHT NOW, don't use breaks bc won't be able to know what smallestPossible, biggestPossible and found are
print("in a list with", str(len(lint)), "elements, we looped",
howManyTimesWeHaveLooked,"times")