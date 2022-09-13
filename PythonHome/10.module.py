# [Module 模組的載入與使用](https://www.youtube.com/watch?v=Et0DjY2cGiE&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=11)
# 載入內建的 sys 模組，並取得資訊
import sys
print(sys.platform)
print(sys.maxsize)

import sys as s # 幫模組取別名
print(s.platform)
print(s.maxsize)

# 調整搜尋模組的路徑(暫時性)
import sys
sys.path.append("Modules") # 在模組的搜尋路徑列表中新增路徑
print(sys.path) # 印出模組的搜尋路徑列表

# 建立 geometry 模組，載入使用
# 需要先建立一個同名的.py檔案
import geometry
result = geometry.distance(1, 1, 5, 5)
print(result)
result = geometry.slope(1, 2, 5, 6)
print(result)

# 調整搜尋模組的路徑(永久性)
# 步驟: 設定/系統/關於/進階系統設定/進階/環境變數/系統變數(新增)
# 變數名稱: PYTHONPATH
# 變數值: (模組資料夾所在的路徑)