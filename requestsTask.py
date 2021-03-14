import requests
import sys

f = open("hosts.txt.txt", "r")
x = []
new_x = []

for i in f:
    x.append(i.split(',')[0])
f.close()

for j in x:
    s = "http://"+j
    try:
        req = requests.get(s,timeout=10)
    except requests.exceptions.RequestException as e:
        print("Error with Req", e)
    except requests.exceptions.Timeout as e2:
        pass
    else:
        st = req.status_code
        if(st == 200):
            new_x.append(s+""+str(st))

new_file = open("newhostfile.txt", 'w')
for i in new_x:
    new_file.write(i+'\n')

new_file.close()

