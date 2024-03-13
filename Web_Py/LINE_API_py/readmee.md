```python

from flask import Flask, render_template
import logging
import requests

app = Flask(__name__)

# 配置日誌處理程序
app.logger.setLevel(logging.ERROR)

# 配置郵件處理程序
# ...

@app.errorhandler(500)
def handle_internal_server_error(error):
    # 發送郵件通知
    # ...

    # 發送郵件通知 Line Notify 請求
    try:
        token = "tokknene"
        message = "下班囉!"

        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = {
            "message": message
        }

        url = "https://notify-api.line.me/api/notify"

        response = requests.post(url, headers=headers, data=data)

        if response.status_code == 200:
            response_content = response.json()
        else:
            print(f"Line Notify request failed with status code {response.status_code}")

    except Exception as e:
        print(f"Failed to send Line Notify request: {e}")

    # 返回自訂一隻訊息
    return render_template("error.html"), 500

# 其他路由.


```