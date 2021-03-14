import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("192.168.1.105", 1234))

message = "This is a test message for Large Data \n"

sock.send(message.encode('utf-8'))
sock.close()
