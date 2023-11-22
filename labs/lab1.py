#print("hello world")

# name_one = input("Enter a person's name:")
# age_one = input("Enter their age:")
# name_two = input("Enter a person's name:")
# age_two = input("Enter their age:")
# if int(age_one)>int(age_two):
#     print(name_one, "is", int(age_one)-int(age_two), "year older than", name_two)
# elif int(age_two)>int(age_one):
#     print(name_two, "is", int(age_two)-int(age_one), "years older than", name_one)
# else:
#     print(name_one, "and", name_two, "are the same age")

# total = 0
# input_number = 0
# while float(input_number)>=0:
#     input_number = input("Enter a number:")
#     if float(input_number) < 0:
#         break
#     total+=float(input_number)
# print(total)

num = []
length = input("How many numbers would you like to enter?")
for x in range(int(length)):
    new_num = input("Enter your number:")
    num.append(float(new_num))

for i in reversed(num):
  print(i)