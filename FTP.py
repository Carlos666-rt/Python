import ftplib
server = ftplib.FTP()
server.connect('192.168.223.130',21,timeout=5)
server.login('aditya','bruhh')