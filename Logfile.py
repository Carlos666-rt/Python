logfile = open("log.txt")
file = logfile.readlines()

for i in file:
    a = (i[:-1].split())
    print(a[-4:])
