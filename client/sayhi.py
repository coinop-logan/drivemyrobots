import socket

server_ip = "34.228.70.168"
server_port = 4546

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(b"Hi!", (server_ip, server_port))

print("sent")