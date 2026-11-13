def func(a, b): # 関数の定義
    if a ** b <= 64: # aのb乗が64以下の場合
        return 1
    else:
        return 0

x = func(4, 3) # 4 ** 3 = 64なので1
y = func(3, 4) # 3 ** 4 = 81なので0
z = [bool(x), bool(y)] # [Ture, False]
print(z)