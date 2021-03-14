import socket
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("192.168.1.105", 1234))
    print("Binded")
    sock.listen(2)
    print("Listening")
    c, adr = sock.accept()
    buffer = 5
    data = " "
    while True:
        packet = c.recv(5)
        parsed = packet.decode()
        data += parsed
        if len(packet) < buffer:
            print("all data have been received")
            print("all data = {}".format(data))
            break

except Exception as e:
    print(e)
