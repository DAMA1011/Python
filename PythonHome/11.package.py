# [Package 封包的設計與使用](https://www.youtube.com/watch?v=GGp-7VHgsKk&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=12)
# 專案檔案配置，路徑概念如下:
# -專案資料夾
#     -主程式.py
#     -封包資料夾
#         -__init__.py  (一定要有的檔案，可以放空)
#         -模組一.py
#         -模組二.py

# import 封包名稱.模組名稱 as 模組別名
# Ex.
# main.py  (主程式)
 # import geometry.point
 # result = geometry.point.distance(3, 4)
 # print(result)

 # import geometry.line as line
 # result = line.slope(1, 1, 3, 3)
 # print(result)

# geometry  (封包資料夾名稱)
# __init__.py  (必要檔案)

# line.py  (模組一名稱)
 # def len(x1, y1, x2, y2):
 #     return ((x2-x1)**2 + (y2-y1)**2)**0.5

 # def slope(x1, y1, x2, y2):
 #     return (y2-y1)/(x2-x1)

# point.py  (模組二名稱)
 # def distance(x, y):
 #     return (x**2 + y**2)**0.5