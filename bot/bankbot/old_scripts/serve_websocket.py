import asyncio
import ssl
import websockets
from setdrive import setDrive

sslContext = ssl.SSLContext(ssl.PROTOCOL_TLS)
sslContext.load_cert_chain(certfile="../keys/botcert.pem", keyfile="../keys/botkey.pem")

async def hello(websocket, path):
    async for message in websocket:
        rawLeft, rawRight = message.split(',')
        left = float(rawLeft)
        right = float(rawRight)
        setDrive(left,right)

asyncio.get_event_loop().run_until_complete(websockets.serve(hello, 'localhost', 8752, ssl=sslContext))

asyncio.get_event_loop().run_forever()