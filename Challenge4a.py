x=input("Enter a String: ")
z=[]
for i in range(len(x)):
    z.append(chr(91 - (ord(x[i])-64)))
z="".join(z)
print(z)