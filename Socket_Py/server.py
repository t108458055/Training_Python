import socket # 導入socket 函式庫
# 調用 socket 中的 socket() 來創建一個socket s
# with 是 py 的語法糖 自動調用 s.close()來銷毀這個 socket. 類似 C# using
#socket.AF_INET => IPv4 協議,  socket.SOCK_STREAM => TCP協定流式協定
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("0.0.0.0", 1234)) # 綁定網口與 Port
    s.listen() # 監聽事件 等待客戶端的連接
    c, addr = s.accept() # c與客戶端進行通訊
    with c:
        print(addr, "connected.")

        while True:
            data = c.recv(1024) # 一次 1024 Byte
            if not data:
                break
            c.sendall(data) # 原封不動將數據回傳給客戶端