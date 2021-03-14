import requests

res = requests.get("http://www.gutenberg.org/cache/epub/1112/pg1112.txt")
a = res.status_code
c = res.text[:10000]
d = res.content
e = res.headers
print(a)
print(c)
f = open("romeo.txt", "wb")
f.write(c.encode())
f.close()
f.close()
