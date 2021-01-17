import sys, json, socket, threading, struct, time

class ClientThread(threading.Thread):
    def __init__(self, port, botID):
        threading.Thread.__init__(self)
        self.botID = botID
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(("0.0.0.0", port))
        print ("New connection started for bot ", botID, "with port", port)

    def run(self):
        _, fromAddr = self.sock.recvfrom(1024)
        while True:
            with open('input_state.json','r') as f:
                inputState = json.load(f)
            botInputState = inputState[self.botID]
            jsonStr = json.dumps(botInputState)
            self.sock.sendto(jsonStr.encode(), fromAddr)
            time.sleep(0.1)

def main():
    helloPort = 4546
    nextClientPort = helloPort + 1

    helloSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    helloSock.bind(("0.0.0.0", helloPort))

    threads = []

    while True:
        print("listening")
        encodedBotID, fromAddr = helloSock.recvfrom(1024) # buffer size is 1024 bytes
        botID = encodedBotID.decode()
        
        print("spawning dedicated connection for", botID, "with port" ,nextClientPort)

        enocodedPort = struct.pack("I", nextClientPort)
        helloSock.sendto(enocodedPort, fromAddr)

        threads.append(ClientThread(nextClientPort, botID))

        nextClientPort += 1

        threads[-1].start()

main()
