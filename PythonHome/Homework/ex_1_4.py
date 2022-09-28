# 輸入一西元年，如2015。判斷此年份是否為閏年。
# 提示：每四年一閏，每百年不閏，每四百年一閏。

year = input("請輸入年份: ")

if int(year) % 4 == 0 & int(year) % 100 != 0:
    print(f'{year} 是閏年')
elif int(year) % 400 == 0:
    print(f'{year} 是閏年')
else:
    print(f'{year} 不是閏年')