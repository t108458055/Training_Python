# importing the relevant libraries
import websockets
import asyncio
# Server data Setting
PORT =  7890 # PORT Set
print("Started server listening on Port " + str(PORT))

# A set of connected ws clients
connected = set()
## # Set: A set is a built-in data structure in Python that represents an unordered collection of unique elements. This means that each element in a set can only appear once, and there is no specific order in which elements are stored. Sets are commonly used when you need to keep track of a collection of items without caring about their order, and you want to ensure that each item is unique within the collection.
# The main behavior function for this server
async def echo(websocket, path):
    print("A client just connected")
    # Store a copy of the connected client
    connected.add(websocket)
    # Handle incoming messages
    try:
        async for message in websocket:
            print("Received message from client: " + message)
            # Send a response ato all connected clients except sender
            for conn in connected:
                if conn != websocket:
                    await conn.send("Someone said:" + message)
    # Handle disconnecting clients
    except websockets.exceptions.ConnectionClosed as e:
        print("Something went wrong!")
        print("A client just disconnected")
        print(e)
    finally:
        connected.remove(websocket)

# Start the server
start_server = websockets.serve(echo, "localhost", PORT)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()