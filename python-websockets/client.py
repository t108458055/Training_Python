# Importing the relevant libraries
import websockets
import asyncio

# The main function that will handle connection and communication 
# with the server
async def listen():
    url = "ws://127.0.0.1:7890"
    # Connect to the server
    try:
        async with websockets.connect(url) as ws:
          # Send a greeting message
          await ws.send("Hello Server!")
          # Stay alive forever, listening to incoming msgs
          while True:
              msg = await ws.recv()
              print(msg)
    except websockets.exceptions.ConnectionClosedOK:
        print("Connection closed gracefully (status code 1000)")
    except Exception as e:
        print(f"An error occurred: {e}")
   

# Start the connection
# asyncio.get_event_loop().run_until_complete(listen())                  # 使用 try，測試內容是否正確
#asyncio.get_event_loop().run_until_complete(listen())
if __name__ == "__main__":
    asyncio.run(listen())
