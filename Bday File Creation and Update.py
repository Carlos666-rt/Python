name = input("Enter your Name: ")
file = open("bday db.txt")
x = 0
z = []
for i in file:
    if(name in i):
        z=i.split(" ")
        print("Your Birthday is",z[1])
        x+=1
        break
if (x==0):
    age=input("Your Birthday is not in Database , Enter your Birthday: ")
    file = open("bday db.txt","a")
    file.write(name +" "+ age +"\n")
    print('DB updated')


