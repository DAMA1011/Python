# 輸入在某商店購物應付金額與實付金額。
# 實付金額小於應付金額，則印出”金額不足”。
# 實付金額等於應付金額，則印出”不必找錢”。
# 實付金額大於應付金額，則輸出找回金額最少的鈔票數和錢幣數。
# 假設幣值只有1000, 500, 100元紙鈔和50, 10, 5, 1元硬幣。
# 說明：若買了132元的商品，付1000元，應找回一張500元，三張100元，一個50元硬幣，一個10元硬幣，一個5元硬幣和三個1元硬幣。

cost = input("請輸入應付金額")

pay = input("實付金額")

if int(cost) > int(pay):
    print("金額不足")
elif int(cost) == int(pay):
    print("不必找錢")
else:
    result = int(pay) - int(cost)
    a = int(result / 1000)
    b = int((result % 1000) / 500)
    c = int(((result % 1000) % 500) / 100)
    d = int((((result % 1000) % 500) % 100) / 50)
    e = int(((((result % 1000) % 500) % 100) % 50) / 10)
    f = int((((((result % 1000) % 500) % 100) % 50) % 10) / 5)
    g = int(((((((result % 1000) % 500) % 100) % 50) % 10) % 5) / 1)

    dict = {a:, b:, c:, d:, e:, f:, g:}

    print(f"須找回{dict}")