# [有序列表的基本運算 - List、Tuple](https://www.youtube.com/watch?v=JLU5oc4_VtA&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=4)
# 有序可變動列表 List []
grades = [12, 60, 15, 70, 90]
print(grades)
print(grades[0]) # 可利用索引查詢列表中的資料
print(grades[1:4])
grades[1:4] = [] # 連續刪除列表中從編號1到編號4(不包括)的資料
print(grades)
grades = [12, 60, 15, 70, 90]
grades[0] = 55 # 把55更換到列表中的第一個位置
print(grades)
grades = grades + [12, 33] # 列表的串接
print(grades)
length = len(grades) # 取得列表的長度，len(列表資料)
print(length)

data = [[3, 4, 5],[6, 7, 8]] # 巢狀列表
print(data[0][1]) # 編號0的資料中，第編號1的資料
data[0][0:2] = [5, 5, 5] # 更換編號0的資料中，從編號0到編號2(不包括)的資料
print(data[0])
print(data)

# 有序不可變動列表 Tuple ()
data = (3, 4, 5) # 除了資料不可以變動之外，其餘操作與 List 相同
print(data[0:2])
data[0] = 5 # 錯誤: Tuple 的資料不可以變動