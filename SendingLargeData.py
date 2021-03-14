import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("192.168.1.105", 1234))
message = "asdkasopdk  asdpaskd[as as[dkasokfpask askdasfjoaifoai saifjaosjfiaoisjfpoajfjaop"
sock.send(message.encode('utf-8'))
sock.close()
