
a = [1, 2, 3, 4]
id_a = id(a)  # オブジェクトaのidを取得
b = a.copy()  # aとは別のオブジェクトを作成
id_d = id(b)
if id_a == id(b):
    result = 'A'
elif id(a) == id(b):
    result = 'B'
elif id_a == id(a):
    result = 'C'
else:
    result = 'D'
print(result)
print(id(a))
print(id_a)
print(type(id_a))