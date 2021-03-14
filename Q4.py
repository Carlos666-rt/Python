Addition = 0
count = 0
F_Name = input("Enter the file name\n")
F_Handle = open("C:/Users/ADITYA/PycharmProjects/pythonProject/" + F_Name, 'r')
for each_line in F_Handle:
    if each_line.startswith("P-Attack-Confirmation:"):
        selected_line = each_line.split(' ')
        Addition = Addition + float(selected_line[1].rstrip("\n"))
        count = count + 1

print("Total occurances are", count)
print("Average is : ", Addition / count)