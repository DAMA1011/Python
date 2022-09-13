# [函式基礎：定義並呼叫函式](https://www.youtube.com/watch?v=7qKFvUVpQXg&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=9)
# 定義函式
# 基本語法:
# def 函式名稱(參數名稱):
#     函式內部的程式碼

# 函式內部的程式碼，若是沒有做函式呼叫，就不會執行
def multiply(n1, n2):
    print(n1*n2)

# # 呼叫函式
multiply(3, 4)
multiply(4, 5)

# 回傳值
# 基本語法:
# def 函式名稱(參數名稱):
#     函式內部的程式碼
#     return

def add(n1, n2):
    print(n1 + n2) # 印出7是從這裡來的
    return # 同沒有打 return 的情況，皆回傳 None

value = add(3, 4) # 這邊要看回傳值是多少
print(value)

def add(n1, n2):
    print(n1 + n2) 
    return 10 # 回傳10的結果

value = add(3, 4) 
print(value)

def add(n1, n2):
    print(n1 + n2) 
    return n1 + n2 # 回傳n1+n2的結果

value = add(3, 4) 
print(value)

def add(n1, n2):
    return n1 + n2 # 直接做回傳n1+n2的結果

value = add(3, 4) 
print(value)

def add(n1, n2):
    return n1 + n2 # 直接做回傳n1+n2的結果

value = add(3, 4) + add(5, 10) # 如果要在函式外部繼續做資料操作的需求，就會使用回傳值的功能
print(value)

# 函式可用來做程式的包裝: 同樣的邏輯可以重複利用
def calculate(max):
    sum = 0
    for n in range(1, max+1):
        sum += n
    print(sum)

calculate(10)
calculate(20)

def  multiply(n1,n2):
        return n1*n2

value = multiply(3,4) + multiply(10,5)
print(value)