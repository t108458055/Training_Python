import requests

token = 'zMmJFPpGzWSLKt6XtyiUfghaZWEAgCASmeKCwYbN1K3'
message = '測試用盲蛇打'

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "message": message
}

url = "https://notify-api.line.me/api/notify"

response = requests.post(url, headers = headers, data = data)

if response.status_code == 200:
    response_content = response.json()
    print(response_content)
else:
    print(f"Request failed with status code {response.status_code}")