# 電力公司使用累計方式來計算電費，分非營業用電及營業用電。
# 輸入何種用電和度數，計算出需繳之電費。(皆以非夏月來計算)

ele = input("請輸入何種用電: ")

num = input("請輸入多少度: ")

# 非營業用函式
def func1(num):
    num_int = int(num)
    if num_int <= 120:
        return num_int*1.63
    if 121 < num_int <=330:
        return num_int*2.10
    if 331 < num_int <= 500:
        return num_int*2.89
    if 501 < num_int <=700:
        return num_int*3.94
    if 701 < num_int <=1000:
        return num_int*4.6
    if 1001 < num_int:
        return num_int*5.03

# 營業用函式
def func2(num):
    num_int = int(num)
    if num_int <= 330:
        return num_int*2.21
    if 331 < num_int <= 700:
        return num_int*2.91
    if 701 < num_int <= 1500:
        return num_int*3.44
    if 1501 < num_int:
        return num_int*5.05

# 利用字典選取要哪一種用電函式
dict_ele = {"非營業用":func1(num), "營業用":func2(num)}

print(int(dict_ele[ele]))