import asyncio
import sys
import json
from collections import defaultdict

bindIP = sys.argv[1]
greetingPort = int(sys.argv[2])
dedicatedPortBase = 50000  # Base port for dedicated connections
nextPort = dedicatedPortBase

active_connections = defaultdict(dict)  # Tracks active connections by bot name

class GreetingHandler(asyncio.Protocol):
    def __init__(self, loop):
        self.loop = loop

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        botID = data.decode().strip()
        print(f"Greeting received from bot: {botID}")

        global nextPort
        assignedPort = nextPort
        nextPort += 1

        # Start a dedicated server for this bot
        asyncio.ensure_future(self.loop.create_server(
            lambda: DedicatedHandler(self.loop, botID),
            bindIP,
            assignedPort
        ))

        # Confirm to the bot that the port is ready
        self.transport.write(f"{assignedPort}".encode())
        print(f"Dedicated port {assignedPort} assigned to bot {botID}")
        self.transport.close()

class DedicatedHandler(asyncio.Protocol):
    def __init__(self, loop, botID):
        self.loop = loop
        self.botID = botID
        self.transport = None
        self.exiting = False

    def connection_made(self, transport):
        self.transport = transport
        active_connections[self.botID]["transport"] = transport
        print(f"Connection established with bot: {self.botID}")
        self.send_input()

    def send_input(self):
        if self.exiting:
            return
            
        try:
            with open('input_state.json', 'r') as f:
                input_state = json.load(f)
            bot_input_state = input_state.get(self.botID, {})
            json_str = json.dumps(bot_input_state)
            self.transport.write(json_str.encode())
            print(f"Sent input to bot {self.botID}: {bot_input_state}")
        except Exception as e:
            print(f"Error sending input to bot {self.botID}: {e}")

        # Schedule the next send
        if not self.exiting:
            self.loop.call_later(0.5, self.send_input)

    def connection_lost(self, exc):
        print(f"Connection lost with bot {self.botID}")
        active_connections.pop(self.botID, None)
        self.exiting = True

    def data_received(self, data):
        print(f"Received from bot {self.botID}: {data.decode()}")

async def main():
    loop = asyncio.get_event_loop()
    server = await loop.create_server(
        lambda: GreetingHandler(loop),
        bindIP,
        greetingPort
    )
    print(f"Greeting server listening on {bindIP}:{greetingPort}")
    await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
