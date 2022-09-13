# [亂數與統計模組](https://www.youtube.com/watch?v=-xwCu6PN1jU&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=14)
# 隨機模組
import random
# 隨機選取
data = random.choice([1, 5, 6, 10, 20])
print(data)
data = random.sample([1, 5, 6, 10, 20], 3) # 可自訂選取數量
print(data)

# 隨機調換順序 
data = [1, 5, 8 ,20]
random.shuffle(data)
print(data)

# 隨機取得亂數
data = random.random() # 0.0 ~ 1.0 之間的隨機亂數
print(data)
data = random.uniform(0.0, 1.0)
print(data)
data = random.uniform(60, 100) # 可自訂區間
print(data)

# 取得常態分配亂數
data = random.normalvariate(100, 10) # 平均數 100，標準差 10，得到的資料多數在 90 ~ 110 之間
print(data)
data = random.normalvariate(0, 5) # 平均數 0，標準差 5，得到的資料多數在 -5 ~ 5 之間
print(data)

# 統計模組
import statistics as stat
data = stat.mean([1, 4, 5, 8]) # 平均數
print(data)
data = stat.median([1, 2, 3, 4, 5, 8, 100]) # 中位數
print(data)
data = stat.stdev([1, 2, 3, 4, 5, 8, 10]) # 標準差
print(data)