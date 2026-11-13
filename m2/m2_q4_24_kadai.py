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