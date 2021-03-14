try:
    a = int(input("Enter number 1"))
    b = input("Enter no 2")
    c = input("Enter a String")
    ans = a//int(b)
    print("The ans is" + str(ans))
    print("Your string is" + int(c))

except ZeroDivisionError as e:
    print("Go Study Mathematics",e,sep="\mMessage by Python Interpretor:")
except TypeError as e2:
    print("Can't Concatinate String and int wtf!You high?",e2)
except ValueError as e3:
    print("Vale error hai bsdk",e3)
except NameError as e4:
    print("Name error i.e no var declared",e4)
print("--------------**********************************************----------------------")
hackeru=


