def put_biggest_at_the_end(aList, upToHere):
    if upToHere > 0:
        next_index_to_look_in = 1
        indexOfBiggest = 0
        while(next_index_to_look_in != upToHere+1):
            # print("comparing at positions", next_index_to_look_in, "and", indexOfBiggest)
        # could we instead use next_index_to_look_in > upToHere?
            if (aList[next_index_to_look_in] > aList[indexOfBiggest]):
                indexOfBiggest = next_index_to_look_in
            next_index_to_look_in +=1
        # print("the biggest one is at index:",indexOfBiggest)
        temp = aList[upToHere]
        aList[upToHere] = aList[indexOfBiggest]
        aList[indexOfBiggest] = temp

    
    # when the while loop is done we want 
    # next_index_to_look_in == upToHere

if __name__ == "__main__":
    l = [33, 5, 37, 24, 91, 0, 1, -1, 200]
    print("original list")
    print(l)

    # we need to turn the following four lines into a function
    biggestIndexToLookAt = len(l)-1
    while(biggestIndexToLookAt!=0):
        put_biggest_at_the_end(l, biggestIndexToLookAt)
        biggestIndexToLookAt -=1
    print(l)

    # put_biggest_at_the_end(l, len(l)-2)
    # print(l)

    # l2 = []
    # put_biggest_at_the_end(l2, len(l2)-1)
    # print(l2)

