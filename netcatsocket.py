import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("0.0.0.0", 4444))
sock.listen(2)
print("Waiting for the connection! You connecting?")
c, addr = sock.accept()

print("Client that tried to connect with me -> {} ".format(addr))

sock.close()
