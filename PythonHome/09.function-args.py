# [函式參數詳解：參數預設值、名稱對應、任意長度參數](https://www.youtube.com/watch?v=OOJmhezLd4o&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=10)
# 基本語法:
# def 函式名稱(參數名稱=預設資料):
#     函式內部的程式碼

def say(msg="Hello"):
    print(msg)
say("Hello Function") # 印出 Hello Function
say() # 印出 Hello

# 參數的預設資料
def power(base, exp=0): # 預設次方不輸入時為0
    print(base**exp)
power(3, 4)
power(4)

# 使用參數名稱對應
def divide(n1, n2):
    print(n1/n2)
divide(2, 4)
divide(n2=2, n1=4) # 使用參數名稱對應時，會忽視參數相對位置

# 無限/不定參數資料
# 基本語法:
# def 函式名稱(*無限參數):
#     函式內部的程式碼

def avg(*num): # 不管輸入多少參數，都能以 Tuple 的方式處理
    print(num) # 以 Tuple 的形式呈現

avg(1, 4, -1, -8) 

def avg(*num):
    for n in num:
        print(n) # 將參數一個一個呈現

avg(1, 4, -1, -8)

def avg(*num):
    sum = 0
    for n in num:
        sum += n
    print(sum/len(num)) # 參數總和除以參數長度，即為平均值 

avg(1, 4, -1, -8)
avg(3, 5, 10)
avg(3, 4)