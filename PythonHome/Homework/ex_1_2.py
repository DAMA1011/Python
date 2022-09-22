time = eval(input("請輸入時數: "))

if time <= 60:
    salary = time*120
if time > 50 & time <= 80:
    salary = 60*120 + (time-60)*120*1.25
if time > 80:
    salary = 60*120 + 20*120*1.25 + (time-80)*120*1.5

print(int(salary))