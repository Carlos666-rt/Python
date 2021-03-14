n = input("Enter words to be Reversed: ")
n = n.split(" ")
for i in range(len(n)):
    n[i] = n[i][::-1]
n = " ".join(n)
print("Reversed String:", n)
