n = input("Enter words for List: ")
n = n.split(" ")
z = []
for i in n:
    z.append(int(i))
z.sort()
z.pop()
print("The Second Biggest Number is", max(z))
