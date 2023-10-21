# Importing the relevant libraries
import websockets
import asyncio

# The main function that will handle connection and communication 
# with the server
async def listen():
    url = "ws://127.0.0.1:7890"
    # Connect to the server
    async with websockets.connect(url) as ws:
        # Send a greeting message
        await ws.send("Hello Server!")
        # Stay alive forever, listening to incoming msgs
        while True:
            msg = await ws.recv()
            print(msg)

# Start the connection
# asyncio.get_event_loop().run_until_complete(listen())
try:                      # 使用 try，測試內容是否正確
  asyncio.get_event_loop().run_until_complete(listen())
except:                   # 如果 try 的內容發生錯誤，就執行 except 裡的內容
    print('發生錯誤')
print('hello')