# print("hello world")
# print("how are you doing?")

#variables---------------------------------------------------------------------------------
# #don't have to assign a type to variables, can't make variable w/o value
# x = 4 #int
# y = x/2 #float, in py 3 & onward, division int/int = float
# print("here's the value of x: ", x)
# print("here's the value of y: ", y)
# y=x//2 #// --> result will be int 
# print("here's the value of y with int division: ", y)

# x = "Jenny" #switches type to string, not int anymore
# print("hello,", x) #comma adds space 
# #can't do y=x/2 anymore bc x is string now

#input--------------------------------------------------------------------------------------
# a_number = input("please enter a number:")  #anything thru input is a string
# print("half of", a_number, "is", int(a_number)//2) 

# #cast (parenthesis around var not "int"), int divison
# #casting doesn't actually change the type of the input, it j returns what it THINKS the string represent
# #so a_number is still a string at this point, good practice to not change value of input 

# another_number =int(input("give me another one: ")) #casts input into int, so another_number is an int
# #if a string is inputed in here ^ will give an error "invalid literal"
# #if a float in inputed in here ^ will give an error bc float != int even when the float is smth like 2.0

# "do not need parenthesis around boolean expression in while and if/else statements. This is valid:"
# "while last_year < user_age: "
# "for this reason, intentation is necessary in python and not java"

#while loops-------------------------------------------------------------------------------------------------
# # print("let's count from one up to your age.")
# # last_year_printed = 0
# # while last_year_printed <user_age:                      can use break statement (break inside'if' inside while breaks while)
# #     last_year_printed +=1                               DO NOT use breaks bc harder to debug, instead use if to make while boolean false so it stops  
# #     print(last_year_printed)                            but if code is vvvv small, break it ok bc doesn't complicate as much, same with continue
# # print("now we are outside the context of the loop")


#lists --------------------------------------------------------------------------------------------------------------------
# a_list=[1,2,3]
# print(a_list) #outputs: [1,2,3] with the brackets
# print(a_list[2]) #outputs 3
# #print(a_list[3]) --> index out of range
# a_list.append("something else")
# print(a_list) #outputs [1,2,3,"something else"]  heterogeneous list, a mix of types even objects

#var name is a pointer/refrence to list
#when putting list in a function, it's a copy(as all vars passed into functions are) of the REFRENCE not the list
#when function modifies a list, it's accessing the one, original list that was created in the calling program via the refrence that gets copied over

#for loops --------------------------------------------------------------------------------------------------------
# for i in a_list:                                    #in order
#     print("here's cone: ",i)                        #anything a for loop can do, so can a while loop but not vise versa

#range(start,stop, step)   start and step are optional, range can only be integers NOT lists
# for i in range(7):
#     print(i)               #outputs 0-6, never goes to 7

# for i in range(-7):    
#     print(i)              #outputs nothing


# for i in range(0,-7,-1): 
#     print(i)             #outputs 0 to-6



#functions -------------------------------------------------------------------------------------------------------
#if var is passed into function, it's a copy  --> means changes to copies only changes copies, not original vars
#if list is passed into function, it's a copy of the refrence  --> means changes to ref reflected in original
#if object (strings are objects but worry abt that later) is passed into function, it's a copy of the refrence  -->means changes to ref reflected in original

#def addOne(x):
#   x=x+1
#   return(x)
#
#x = 1
#addOne(x)
#print(x)    #prints 1 bc x in addOne() and x outside of it are diff x, the x in the function only comes into existance once x is defined (x=x+1)
#--------------------------------
# def addOne(x):
#     x=x+1
#     return(x)

# x = 1
# print(addOne(x))    #prints 2 
#--------------------------------------
# def addOne(x):
#     print(x)
# x = 1
# print(x)   #prints 2 1's. One from the function and one from var x. Uses a copy of var x in the function to print
#----------------------------------------
# def addOne():
#     print(x)

# x=1
# addOne()      #no error, x is a global var, prints 1
#----------------------------------------------------------
# def addOne():
#      print(x+1)

# x=1
# addOne()  
#print(x)                 #no error, uses x here bc no x in the function so looks for another var to use. x is a global var, prints 2 

# if import a file, if there's an x in there might be able to use it* not sure       
#---------------------------------------------------------------------------------
# def addOne():
#     return(x+1)

# x=1
# addOne()      
# print(x)      #prints 1
#--------------------------------------
# def addOne():
#     x=x+1
#     return(x)

# x=1
# addOne()      
# print(x)               #error bc x is trying to be defined in the function w/ outside x

#AVOID GLOBAL VARS!!

#objects---------------------------------------------------------------------------------------------------
#objcts consists of collection of attributes and methods that operate on those attributes