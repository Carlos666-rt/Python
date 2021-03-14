import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("192.168.1.105", 4444))
print("Binded")
sock.listen()
print("Listening")
c, addr = sock.accept()
data = c.recv(2048)
print(data.decode())
print("Client that tried to connect with me -> {} ".format(addr))
message = "What should i do"
c.send(message.encode("utf-8"))
sock.close()
