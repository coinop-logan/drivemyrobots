import socket, threading, struct

class ClientThread(threading.Thread):
    def __init__(self, port):
        threading.Thread.__init__(self)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(("0.0.0.0", port))
        print ("New connection started with port ", port)

    def run(self):
        print("listening again")
        data, from_addr = self.sock.recvfrom(1024)
        print("received! %s" % data)
        self.sock.sendto(b"hi again", from_addr)

hello_port = 4546
next_client_port = 4547

hello_sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
hello_sock.bind(("0.0.0.0", hello_port))

threads = []

while True:
    data, from_addr = hello_sock.recvfrom(1024) # buffer size is 1024 bytes
    print("received hello: %s" % data)
    print("spawning connection with port %s" % str(next_client_port))

    send_data = struct.pack("I", next_client_port)
    hello_sock.sendto(send_data, from_addr)

    threads.append(ClientThread(next_client_port))

    next_client_port += 1

    threads[-1].start()
