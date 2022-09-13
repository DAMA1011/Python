# [類別的定義與使用 - Class Attributes](https://www.youtube.com/watch?v=uPKgQ3FoVtY&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=16)
# 類別的第一種用法:
# 定義類別，與類別屬性(封裝在類別中的變數和函式)

# 基本語法:
# class 類別名稱:
#     定義封裝的變數
#     定義封裝的函式

# 定義一個類別 IO，有兩個屬性 supportedSrcs 和 read
class IO:
    supportedSrcs = ["console", "file"]
    def read(src):
        if src not in IO.supportedSrcs:
            print("Not Supported")
        else:
            print("read from", src)

# 使用類別
print(IO.supportedSrcs)
IO.read("file")
IO.read("internet")