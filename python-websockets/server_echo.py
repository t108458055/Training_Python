# importing the relevant libraries
import websockets
import asyncio

PORT =  7890

print("Started server listening on Port " + str(PORT))

async def echo(websocket, path):
  print("A client just connected")
  try:
      async for message in websocket:
          print("Received message from client: " + message)
          await websocket.send("Response(Pong):" + message)
  except websockets.exceptions.ConnectionClosed as e:
      print("Something went wrong!")
      print("A client just disconnected")
      print(e)

start_server = websockets.serve(echo, "localhost", PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()