def naame(l):
    name = l[0]
    a = int(l[1])
    b = int(l[2])
    s = a + b
    print("The sum of values {} and {} entered by user {} is {} ".format(a, b, name, s))

name_u1= input("Enter your name and 2 values to add")
naame(name_u1.split())
