from ftplib import FTP
server = FTP("192.168.223.130")
server.login()
user = input("Enter File with .txt extention to be uploaded")
file = open("{}".format(user))
file = open("{}".format(user),"rb")
server.storbinary("STOR {}".format(user), file)
file.close()
server.quit()
