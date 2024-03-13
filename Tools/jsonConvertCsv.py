import csv
import json
# 從json文件讀取數據
with open('D:\*.json', 'r', encoding='utf-8-sig') as json_file:
    data = json.load(json_file)
# 提取 "Name" 和 "Comment" 字段
extracted_data = []
for item in data:
    extracted_data.append({
        "Name": item["Name"],
        "Comment": item["Comment"]
    })
# 提取數據並寫入csv
with open('csnase0927(2).csv', 'w', newline='', encoding='utf-8-sig') as csv_file:
    fieldnames = ["Name", "Comment"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    #寫入csv文件 標題行
    writer.writeheader()
#寫曲提取的數據
    for item in extracted_data:
        writer.writerow(item)