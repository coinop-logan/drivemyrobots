import asyncio, sys, json

bindIP = sys.argv[1]
requestPort = sys.argv[2]

class RequestHandler:
    def __init__(self, loop):
        self.loop = loop
    
    def connection_made(self, transport):
        self.transport = transport
    
    def datagram_received(self, data, addr):
        botID = data.decode()
        botAddress = addr
        print("connection:", botAddress, botID)
        updater = self.loop.create_datagram_endpoint(
            lambda: BotUpdater(loop, botID),
            remote_addr = (botAddress[0], 4546)
        )
        updaterTask = loop.create_task(updater)


class BotUpdater:
    def __init__(self, loop, botID):
        self.loop = loop
        self.botID = botID
    
    def connection_made(self,transport):
        self.transport = transport
        self.loop.call_soon(self.sendInput)
    
    def sendInput(self):
        with open('input_state.json','r') as f:
            inputState = json.load(f)
        botInputState = inputState[self.botID]

        jsonStr = json.dumps(botInputState)
        self.transport.sendto(jsonStr.encode())
        self.loop.call_later(0.5,self.sendInput)
    
    def error_received(self, exc):
        print("error recieved:", exc)
        

loop = asyncio.get_event_loop()

listen = loop.create_datagram_endpoint(
    lambda: RequestHandler(loop),
    local_addr = (bindIP,requestPort)
)
transport, protocol = loop.run_until_complete(listen)

loop.run_forever()
transport.close()
loop.close()