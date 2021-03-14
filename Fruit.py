x=int(input())
result=[]
for i in range(x):
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    minn = min(a,b)
    maxx = max(a,b)

    while (minn<maxx and c>0):
        minn = minn + 1

        c = c - 1
        print(minn,maxx,c)
    result.append(max(a,b) - minn)

for i in result:
    print(i)
