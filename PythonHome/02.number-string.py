# [數字、字串的基本運算](https://www.youtube.com/watch?v=bLRa4TZ99aY&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=3)
# 數字運算
x = 9 + 2
print(x)
x = 9 - 2
print(x)
x = 9*2
print(x)
x = 9/2
print(x)
x = 9//2 # 取整數
print(x)
x = 9%2 # 取餘數
print(x)
x = 9**2 # 次方
print(x)
x = 2 + 3
print(x)
x += 1 # x = x + 1 ，將變數中的數字+1 
print(x)

# 字串運算
s = "Hello"
print(s)
s = "Hell\"o" # 如果要在字串內加入引號，則前面需要加\，此為跳脫
print(s)
s = "Hello" + "World"
print(s)
s = "Hello" "World" # 在 python 裡，一個空格也視為字串的串接
print(s)
s = "Hello\nWorld"
print(s)
s = """Hello
World""" # 在 python 裡，用三個雙引號或三個單引號，即可換行
print(s)
s = "Hello"*3 + "World" #先乘除後加減
print(s)
s = "Hello" # 字串會對內部的字元編號(索引)，從0開始算起
print(s[0])
print(s[1:4]) # 包含起始編號，不包含結尾編號
print(s[:4]) # 從頭算起，不包含結尾編號
print(s[1:]) # 從起始編號算起，取後面全部