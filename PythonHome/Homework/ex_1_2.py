# 輸入便利商店工讀生的工作時數，並計算其薪資。
# 60小時以內，時薪150元。
# 61~80小時，以時薪1.25倍計算。
# 81小時以上，以時薪1.5倍計算。
# 說明：薪資以累計方式計算。若工時為90小時，則薪資為60*150 + 20*150*1.25 + 10*150*1.5元。

time = eval(input("請輸入時數: "))

if time <= 60:
    salary = time*120
if time > 50 & time <= 80:
    salary = 60*120 + (time-60)*120*1.25
if time > 80:
    salary = 60*120 + 20*120*1.25 + (time-80)*120*1.5

print(int(salary))