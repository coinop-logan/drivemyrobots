import socket

server_ip = "34.228.70.168"
hello_port = 4546

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(b"Hi!", (server_ip, hello_port))

print("sent, listening")