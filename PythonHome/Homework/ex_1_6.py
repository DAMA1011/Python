# 一元二次方程式ax2+bx+c=0。輸入a, b, c三值，並計算方程式的根。
# b2-4ac > 0，有兩個不相等的實根。
# b2-4ac = 0，有兩個相等的實根。
# b2-4ac < 0，則印出”沒有實根”。

str_a = input("請輸入值a: ")
str_b = input("請輸入值b: ")
str_c = input("請輸入值c: ")

a = int(str_a)
b = int(str_b)
c = int(str_c)

result = (b**2) - (4*a*c)
if result < 0:
    print("沒有實根")
elif result == 0:
    x = (-b) / (2*a)
    print(f"有兩個相等的實根:{x}")
else:
    x = (-b + result**0.5) / (2*a)
    y = (-b - result**0.5) / (2*a)
    print(f"有兩的不相等的實根:{x},{y}")