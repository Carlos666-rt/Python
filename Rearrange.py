n = input("Enter words for List: ")
n = n.split(" ")
n.sort()
print(n)
for i in range(len(n)):
    n[i] = n[i][::-1]
print(n)
