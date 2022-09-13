# [文字檔案的讀取和儲存](https://www.youtube.com/watch?v=C4OkV6DrVRs&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=13)
# 基本語法:
# 檔案物件 = open(檔案路徑, mode=開啟模式)

# 常用模式:
#   讀取 r
#   寫入 w
#   讀寫 r+

# 讀取全部內容:
# 檔案物件.read()

# 一次讀取一行:
# for 變數 in 檔案物件:
#     從檔案依序讀取每行文字到變數中

# 寫入文字:
# 檔案物件.write(字串)

# 關閉檔案:
# 檔案物件.close()

# 儲存檔案(傳統寫法)
file = open("data.txt", mode="w", encoding="utf-8") # 開啟，中文編碼(encoding="utf-8")
file.write("Hello File\nSecond Line\n測試中文") # 操作
file.close() # 關閉

# 最佳寫法(區塊會自動、安全的關閉檔案，不須寫close):
# with open(檔案路徑, mode=開啟模式) as 檔案物件

# 儲存檔案(最佳寫法)
with open("data.txt", mode="w", encoding="utf-8") as file:
    file.write("Hello File\nSecond Line\n測試中文")

with open("data1.txt", mode="w", encoding="utf-8") as file:
    file.write("3\n5\n12\n9")

# 讀取檔案
with open("data.txt", mode="r", encoding="utf-8") as file:
    data = file.read()
print(data)

sum = 0 # 把檔案中的數字資料，一行一行的讀取出來，並計算總合
with open("data1.txt", mode="r", encoding="utf-8") as file:
    for line in file: # 一行一行的讀取
        sum += int(line) # 計算總合
print(sum)

# 讀取 JSON 格式:
# 讀取到的資料 = json.load(檔案物件)

# 寫入 JSON 格式:
# json.dump(要寫入的資料, 檔案物件)

# 使用 JSON 格式讀取，複寫檔案
import json
# 從檔案中讀取 JSON 資料，放入變數 data 裡面
with open("config.json", mode="r") as file:
    data = json.load(file)
print(data) # data 是一個字典資料
print("name", data["name"])
print("version", data["version"])

data["name"] = "new name" # 修改變數中的資料
# 把最新的資料複寫回檔案中
with open("config.json", mode="w") as file:
    json.dump(data, file)