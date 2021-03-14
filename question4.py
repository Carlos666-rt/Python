f = input("Enter file name: ")
file = open("C:/Users/ADITYA/PycharmProjects/pythonProject/{}".format(f))
l = []
n = 0
count = 0
for i in file:
    if i.startswith("P-Attack"):
        s = i.split()
        n = n+float(s[1])
        count = count+1
print("Attack confidence is: ", n/count)
print("Total Occurance is:", count)