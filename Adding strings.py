s = input("Enter a String\n")

while (len(s) < 10):
    a = input("Enter more value, The length value is %s\n" % len(s))
    s = s + a

    a = ""
    print(s)
