# 老王養了一群兔子，若三隻三隻一數，剩餘一隻；若五隻五隻一數，剩餘三隻；若七隻七隻一數，剩餘二隻。試問兔子最少有幾隻。

num = 1
while not(num % 3 == 1 and num % 5 == 3 and num % 7 == 2):
    num += 1
    
print(num)