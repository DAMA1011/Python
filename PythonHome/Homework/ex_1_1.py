# 輸入月份1~12月，利用switch判斷相對應的季節春、夏、秋、冬並印出。若不在此範圍則印出”輸入錯誤”。

num = eval(input("請輸入月份: "))

dict = {3 : "春天", 4 : "春天", 5 : "春天", 6 : "夏天", 7 : "夏天", 8 : "夏天", 9 : "秋天", 10 : "秋天", 11 : "秋天", 12 : "冬天", 1 : "冬天", 2 : "冬天"}

print(dict[num])