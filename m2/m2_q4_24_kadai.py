def func(a, b): 
    if a ** b <= 64: 
        return 1
    else:
        return 0

x = func(4, 3)
y = func(3, 4) 
a = func(-5, -6)
z = [bool(x), bool(y), bool(a)] 
print(z)

'''bool関数について
bool()は値をTrueまたはFalseに変換する関数
0はFalse,それ以外の数値はTrueになる
'''