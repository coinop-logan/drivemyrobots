import socket, struct

server_ip = "34.228.70.168"
hello_port = 4546

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind(("0.0.0.0", hello_port))
sock.sendto(b"Hi!", (server_ip, hello_port))

print("sent, listening")

data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
print("received message: %s" % data)

dedicated_port = struct.unpack("I", data)[0]

newsock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("sending to", server_ip ,dedicated_port)
newsock.bind(("0.0.0.0", dedicated_port))
newsock.sendto(b"hi again!!!", (server_ip, dedicated_port))

data, addr = newsock.recvfrom(1024)
print("received another message: %s" % data)