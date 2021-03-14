N=input("Enter the String:")
x=[]
y=[]
z=[]
p=[]
l=[]
for i in N:
   if i.isalpha(): z.append(i)
   elif int(i) % 2==0:
      x.append(i)
   else:
      y.append(i)
p=sorted(y)
l=sorted(x)
o=z[::-1]+p+l
print("The Output of the given alpha_Numerical String:","".join(o))