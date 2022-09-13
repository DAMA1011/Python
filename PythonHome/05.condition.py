# [流程控制：if 判斷式](https://www.youtube.com/watch?v=A93BsHB-lWo&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=6)
# 判斷式
if True:
    print("True 執行")
else:
    print("False 執行")

x = input("請輸入數字: ") # 取得"字串形態"的使用者輸入
x = int(x) # 將字串型態轉換成"整數型態"
if x>200:
    print("大於 200")
elif x>100:
    print("大於 100,小於等於 200")
else:
    print("小於等於 100")

# 四則運算
n1 = int(input("請輸入數字一: "))
n2 = int(input("請輸入數字二: "))
op = input("請輸入運算: +, -, *, /: ")
if op == "+":
    print(n1+n2)
elif op == "-":
    print(n1-n2)
elif op == "*":
    print(n1*n2)
elif op == "/":
    print(n1/n2)
else:
    print("不支援的運算")