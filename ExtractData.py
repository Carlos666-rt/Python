import urllib.request

url = urllib.request.urlopen("https://raw.githubusercontent.com/noobsecurity/sample_data/master/log.txt")
a = url.read().decode()
b = (a.split("\n"))
c = 1
for i in range(len(b)):
    z = (b[i].split(" "))
    if (z[0] == "From"):
        print(c, z[1])
        c += 1
