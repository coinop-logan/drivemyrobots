import socket, sys, bot_driver, json, time, struct

serverIP = sys.argv[1]
helloPort = 4546

def main():
    print("setting up bot...")
    bot_driver.setup()

    encodedBotID = bot_driver.botID.encode()

    print("contacting server...")
    helloSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    helloSocket.bind(("0.0.0.0", helloPort))
    helloSocket.sendto(encodedBotID, (serverIP, helloPort))

    print("listening for response...")
    dedicatedPortData, _ = helloSocket.recvfrom(1024)
    dedicatedPort = struct.unpack("I", dedicatedPortData)[0]

    print("reconnecting to dedicated port %i..." % dedicatedPort)
    newsock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    print("sending to", serverIP ,dedicatedPort)
    newsock.bind(("0.0.0.0", dedicatedPort))
    newsock.sendto(encodedBotID, (serverIP, dedicatedPort))

    print("starting drive loop")
    lastInputState = {}
    while True:
        driveData, _ = newsock.recvfrom(1024)
        inputState = json.loads(driveData.decode())
        if inputState != lastInputState:
            bot_driver.enactInput(inputState)

main()