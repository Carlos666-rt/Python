
my_list = input(int("Enter 1st no"))
my_list2 = input(int('Enter 2nd no'))

result = list(filter(lambda x: (x % my_list == 0), my_list))
result2 = list(filter(lambda x: (x % my_list2 == 0), my_list2))

# display the result
print("Numbers divisible by 13 are",result)