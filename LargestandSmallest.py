lst = []
while True:
    x = input("Enter a number: ")
    if x == "completed":
        break
    else:
        try:
            x = int(x)
            lst.append(x)
        except ValueError:
            print("Invalid input")
print("Maximum Number is", max(lst))
print("Minimum Number is", min(lst))
