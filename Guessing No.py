import random
x= int(random.randint(1,10))
n = int(input("Enter a No: "))
print("The answer is",x)
if (n<x):
    print ("Your Guess is lower,guess higher")
elif(n>x):
    print ("Your Guess is higher , Guess lower")
elif(n==x):
    print ("You have guessed it right")