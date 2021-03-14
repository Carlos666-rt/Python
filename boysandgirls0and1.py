t = int(input())
l = ""
m = ""
o = []
for i in range(0,t):
    k = 0
    num1 = input()
    num2 = input()
    f = num2.count("1")
    s = num2.count("0")
    for j in num2:
        if j == "1":
            l = l +j
            k = k+1
        else:
            m = m+j
    o.append(k)
for i in o:
    print(i)