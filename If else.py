Name = input("Enter your name")
age = int(input("Enter your age?\n"))

if Name == "Alice":
    print("Hi Alice")
else:pass

if age < 12:
    print("You are not Alice kid")
    exit()
elif age > 2000:
    print("Jhoot")
    exit()
elif age == 18:
    print("True")
    exit()
