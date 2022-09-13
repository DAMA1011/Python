# [實體物件的建立與使用 - 上篇 - 實體屬性 Instance Attributes](https://www.youtube.com/watch?v=Lr5N2r1rmtM&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=17)
# 類別的第二種用法:
# 定義類別，與實體物件，與實體屬性
# 觀念: 先定義類別，再透過類別建立實體物件，然後才能使用實體屬性

# 建立實體物件
# 基本語法:
# class 類別名稱:
#     def __init__(self):   # 定義初始化函式
#         透過操作 self 來定義實體屬性
# obj = 類別名稱()   # 建立實體物件，呼叫初始化函式，放入變數 obj 中

# 使用實體屬性
# 基本語法:
# 實體物件.實體屬性名稱

# Point 實體物件的設計: 平面座標上的點
class Point:
    def __init__(self): # 定義初始化函式
        self.x = 3 # 操作 self 來定義實體屬性
        self.y = 4
p1 = Point() # 建立實體物件
print(p1.x, p1.y) # 使用實體屬性

class Point:
    def __init__(self, x, y): 
        self.x = x
        self.y = y
# 建立第一個實體物件
p1 = Point(5, 6) 
print(p1.x, p1.y) 
# 建立第二個實體物件
p2 = Point(7, 8)
print(p2.x, p2.y)

# FullName 實體物件的設計: 分開紀錄姓、名資料的全名
class FullName:
    def __init__(self, first, last):
        self.first = first
        self.last = last
name1 = FullName("K.H.", "Lin")
print(name1.first, name1.last)
name2 = FullName("W.C.", "Chen")
print(name2.first, name2.last)