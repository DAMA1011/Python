# [實體物件的建立與使用 - 下篇 - 實體方法 Instance Methods](https://www.youtube.com/watch?v=MZtTClJ74NU&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=18)
# 類別的第二種用法(擴增):
# 定義類別，與實體物件，與實體屬性，與實體方法
# 觀念: 先定義類別，再透過類別建立實體物件，然後才能使用實體屬性以及實體方法

# 建立實體物件
# 基本語法:
# class 類別名稱:
#     def __init__(self):   # 定義初始化函式
#         透過操作 self 來定義實體屬性
#     def 實體方法名稱(self, 自訂參數):   # 定義實體方法/函式
#         實體方法主體   # 透過 self 操作實體物件
# obj = 類別名稱()   # 建立實體物件，呼叫初始化函式，放入變數 obj 中

# 呼叫實體方法
# 基本語法:
# 實體物件.實體方法名稱(參數資料)

# Point 實體物件的設計: 平面座標上的點
class Point:
    def __init__(self, x, y): # 定義初始化函式
        self.x = x # 操作 self 來定義實體屬性
        self.y = y
    def show(self): # 定義實體方法/函式
        print(self.x, self.y) # 透過 self 操作實體物件
p = Point(1, 5) # 建立實體物件
p.show() # 呼叫實體方法

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self): # 可以定義多個實體方法
        print(self.x, self.y)
    def distance(self, targetX, targetY):
        return (((self.x-targetX)**2) + ((self.y-targetY)**2))**0.5
p = Point(3, 4)
p.show()
result = p.distance(0, 0) # 計算座標(3, 4)跟座標(0, 0)之間的距離
print(result)

# File 實體物件的設計: 包裝檔案讀取的程式
# 觀念: 把比較複雜的 code 包裝在類別中，利用實體物件來操作
class File:
    def __init__(self, name):
        self.name = name
        self.file = None # 尚未開啟檔案: 初期是 None
    def open(self):
        self.file = open(self.name, mode="r", encoding="utf-8")
    def read(self):
        return self.file.read()
# 讀取第一個檔案
f1 = File("data.txt")
f1.open()
data = f1.read()
print(data)
# 讀取第二個檔案
f2 = File("data1.txt")
f2.open()
data = f2.read()
print(data)