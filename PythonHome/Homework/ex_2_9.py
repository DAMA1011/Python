# 畫出下列三種排列的星星圖形。
# (1)     (2)      (3)
# *       *****        *
# **       ****       ***
# ***       ***      *****
# ****       **     *******
# *****       *    *********

n = 10 # 在此調整層數

for i in range(n): # 圖形 1
    i += 1
    j = 0
    while j < i:
        j += 1
        print("*", end="")
    print("")

print("---------------------")

for i in range(n): # 圖形 2
    j = 0
    while j < i:
        j += 1
        print(" ", end="")
    j = 0
    while (j + i) < n:
        j += 1
        print("*", end="")
    print("")

print("---------------------")

for i in range(n): # 圖形 3
    j = 1
    while (j + i) < n:
        j += 1
        print(" ", end="")
    j = 1
    while j <= (2*i + 1):
        j += 1
        print("*", end="")
    print("")