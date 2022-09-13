# [流程控制：迴圈基礎，while 迴圈、for 迴圈](https://www.youtube.com/watch?v=szaAeLt_49U&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=7)
# while 迴圈
n = 1
sum = 0 # 1+2+3+...+10
while n<=10:
    sum = sum + n # 紀錄累加的結果
    n += 1
print(sum)

# for 迴圈
for x in [3, 5, 1]:
    print(x)
for y in "taiwan":
    print(y)
for z in range(5):
    print(z)
for k in range(2, 10):
    print(k)
sum = 0 # 1+2+3+...+10
for m in range(1, 11):
    sum = sum + m
print(sum)