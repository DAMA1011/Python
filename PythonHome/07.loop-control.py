# [流程控制：迴圈進階控制，break、continue、else 命令](https://www.youtube.com/watch?v=yBXlwOmLqZ4&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=8)
# break(強制結束迴圈)
# 基本語法:
# while 布林值:
#     break
# for 變數名稱 in 列表或字串:
#     break

# break 的簡易範例
n = 0
while n<5:
    if n == 3:
        break # 強制結束迴圈
    print(n) # 印出迴圈中的n
    n += 1
print("最後的 n: ", n) # 印出迴圈結束後的n

# continue(強制繼續下一圈)
# 基本語法:
# while 布林值:
#     continue
# for 變數名稱 in 列表或字串:
#     continue

# continue 的簡易範例
m = 0
for x in [0, 1, 2, 3]:
    if x%2 == 0: # x可以被2整除
        continue # 強制進入下一迴圈
    print(x)
    m += 1
print("最後的 m: ", m)

# else 的簡易範例
sum = 0
for n in range(11):
    sum += n
else: # 迴圈結束前，執行此區塊的命令
    print(sum) # 印出0+1+2+3+...+10的結果

# 綜合範例: 找出整數平方根
# 輸入9，得到3
# 輸入7，得到沒有整數的平方根
n = input("請輸入一個正整數: ")
n = int(n) # 轉換成數字
for i in range(n): # i從0 ~ n-1
    if i*i == n:
        print("整數平方根", i)
        break # 用 break 強制結束迴圈時，不會執行 else 區塊
else:
    print("沒有整數平方根")