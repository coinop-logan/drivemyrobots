import asyncio, sys, json, time

ip = sys.argv[1]
port = sys.argv[2]

class RequestMaker:
    def __init__(self, loop, botID):
        self.loop = loop
        self.botID = botID
        self.transport = None
    
    def connection_made(self, transport):
        self.transport = transport
        self.transport.sendto(self.botID.encode())
    
    def error_received(self, exc):
        print('Error received:', exc)

    def connection_lost(self, exc):
        print("Connection closed")


# class InputReceiver:
#     def __init__(self, loop):
#         self.loop = loop
#         self.transport = None
#         self.inputState = None
#         self.lastCommandReceivedTime = 0
#         self.exiting = False
    
#     def connection_made(self, transport):
#         self.transport = transport
#         self.loop.call_soon(self.runBotForever)
    
#     def datagram_received(self, data, addr):
#         self.inputState = json.loads(data.decode())
#         self.lastCommandReceivedTime = time.time()
    
#     def runBotForever(self):
#         if self.lastCommandReceivedTime + 1 > time.time():
#             if self.inputState:
#                 bot_driver.enactInput(self.inputState)
#         if not self.exiting:
#             self.loop.call_soon(self.runBotForever)

#     def error_received(self, exc):
#         print('Error received:', exc)
#         bot_driver.close()
#         self.exiting = True

#     def connection_lost(self, exc):
#         print("Connection closed")
#         bot_driver.close()
#         self.exiting = True

def main():

    loop = asyncio.get_event_loop()

    makeRequest = loop.create_datagram_endpoint(
        lambda: RequestMaker(loop, "bigbot"),
        remote_addr = (ip,port)
    )
    transport1, protocol1 = loop.run_until_complete(makeRequest)

    # receiveInput = loop.create_datagram_endpoint(
    #     lambda: InputReceiver(loop),
    #     local_addr = ("192.168.1.105",4546)
    # )

    # transport2, protocol2 = loop.run_until_complete(receiveInput)

    loop.run_forever()
    transport1.close()
    loop.close()

    asyncio.run(main())

main()