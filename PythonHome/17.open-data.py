# [網路連線程式、公開資料串接](https://www.youtube.com/watch?v=sUzR3QVBKIo&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=15)
# 模組: urllib.request
# 基本語法:
# import urllib.request as request
# with request.urlopen(網址) as response:
#     data = response.read()
# print(data)

# 資料格式 JSON: 使用內建的 json 模組

# 網路連線
import urllib.request as request
url = "http://www.ntu.edu.tw/" # 抓取台大網頁的原始碼
with request.urlopen(url) as response:
    data = response.read().decode("utf-8")
print(data)

# 串接、擷取公開資料
import urllib.request as request
import json
url = "https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire" # 抓取台北市政府資料開放平台網頁的原始碼
with request.urlopen(url) as response:
    data = json.load(response) # 利用 json 模組處理 json 資料格式
print(data)

# 取得公司名稱，並新增一個 txt 檔案
clist = data["result"]["results"]
print(clist)

with open("data2.txt", mode="w", encoding="utf-8") as file:
    for company in clist:
        file.write(company["公司名稱"]+"\n")