a = [1, 2, 3, 4]
id_a = id(a) # id()関数はオブジェクトaのidを取得し、id_aに代入
b = a.copy() # aのcopyを作成し、bに代入する(aとは別のオブジェクトとなる)
id_d = id(b) # bのidを取得し、id_dに代入
if id_a == id(b): # False:　aとbは別のオブジェクトなので、idも異なる
    result = 'A'
elif id(a) == id(b): #　False: aとbは別のオブジェクトなので、idも異なる
    result = 'B'
elif id_a == id(a): # True: id_aにはid(a)の戻り値が代入される
    result = 'C'
else: # 上記の条件がいずれかがTrueになるため実行されない
    result = 'D'
print(result) # C

"""ノート
Pythonのid()関数は、オブジェクトを識別するための整数値(init)を返す

"""