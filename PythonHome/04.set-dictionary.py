# [集合、字典的基本運算 - Set、Dictionary](https://www.youtube.com/watch?v=L3-KuGYhw78&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=6)
# 集合的運算
s1 = {3, 4, 5}
print(3 in s1)
print(4 not in s1)
s1 = {3, 4, 5}
s2 = {4, 5, 6, 7}
s3 = s1&s2 # 交集: 取兩個集合中，相同的資料
print(s3)
s3 = s1|s2 # 聯集: 取兩個集合中，所有的資料，但不重複取
print(s3)
s3 = s1-s2 # 差集: 從s1中，減去和s2重疊的部分
print(s3)
s3 = s1^s2 # 反交集: 取兩個集合中，不重疊的部分
print(s3)

s = set("Hello") # set(字串)，將字串拆解成集合，不包含重複的部分，且沒有順序
print(s)
print("H" in s)
print("a" in s)

# 字典的運算
dic = {"apple":"蘋果", "orange":"橘子"}
print(dic["apple"])
dic["apple"] = "小蘋果"
print(dic["apple"])
print("apple" in dic) # 只能判斷 key 是否存在，無法判斷 value 是否存在
print("蘋果" in dic)

dic = {"apple":"蘋果", "orange":"橘子"}
print(dic)
del dic["apple"] # 刪除字典中的鍵值對(key-value pair)
print(dic)

dic = {x:x*2 for x in [3, 4, 5]} # 從列表的資料產生字典，此為固定語法(.:. for . in 列表)
print(dic)