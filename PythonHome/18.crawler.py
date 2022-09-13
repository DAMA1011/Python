# [網路爬蟲 Web Crawler 基本教學](https://www.youtube.com/watch?v=9Z9xKWfNo7k&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=19)
# 基本流程: 1.連線到特定網址，抓取資料
#           2.解析資料，取得實際想要的部份

# 資料格式: 1.JSON: 使用內建的 json 模組
#           2.HTML: 使用第三方套件 BeautifulSoup

# 安裝方法: 使用 PIP 套件管理工具，pip install beautifulsoup4

# 抓取 PTT 電影版的網頁原始碼(HTML)
# 錯誤寫法:
import urllib.request as req
url = "https://www.ptt.cc/bbs/movie/index.html"
with req.urlopen(url) as response:
    data = response.read().decode("utf-8")
print(data) # 這樣的輸出結果會顯示連線被拒絕(Forbidden)，是因為這種寫法不像正常人在逛網頁的樣子，會被網頁阻擋

# 正確寫法:
import urllib.request as req
url = "https://www.ptt.cc/bbs/movie/index.html"
# 建立一個 request 物件，附加 Request Headers 的資訊
request = req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54"
})
with req.urlopen(request) as response: # open 不要直接給 url，而是給 request，利用 request 打開網址
    data = response.read().decode("utf-8")
print(data)

# 解析原始碼，取得每篇文章的標題
import bs4
root = bs4.BeautifulSoup(data, "html.parser") # 利用 BeautifulSoup 協助我們解析 HTML 格式文件
print(root.title) # 抓取網頁標籤
print(root.title.string) # 抓取網頁標籤內的文字

titles = root.find("div", class_="title") # 尋找 class="title" 的 div 標籤，並且只找第一個
print(titles.a.string) # 抓取 a 標籤內的文字

titles = root.find_all("div", class_="title") # 尋找 class="title" 的 div 標籤，並且找到全部，以 list 形式呈現
for title in titles:
    if title.a != None: # 如果標題包含 a 標籤(沒有被刪除)，則印出來
        print(title.a.string)