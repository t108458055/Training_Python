import socket # 導入socket 函式庫
# 調用 socket 中的 socket() 來創建一個socket s
# with 是 py 的語法糖 自動調用 s.close()來銷毀這個 socket. 類似 C# using
#socket.AF_INET => IPv4 協議,  socket.SOCK_STREAM => TCP協定流式協定
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("127.0.0.1", 1234)) # 連線網口與 Port
    s.sendall(b"Hello, Andy!!")  #要傳送的字串
    data = s.recv(1024) # 接收回 1024 byte
    print("Received:", repr(data))
  