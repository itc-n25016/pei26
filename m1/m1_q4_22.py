a = 17
b = 5
dm = divmod(a, b) 
p = pow(dm[0], dm[1]) # p = 3 ** 2 = 9
all_num = [a + b + dm[0] + dm[1] + p] # [17, 5, 3, 2, 9]
min_all = min(all_num) # 2
max_all = max(all_num) # 17
sum_all = sum(all_num) # 36
print(f'{min_all}, {max_all}, {sum_all}')

'''ノート
divmod()関数とは、2つの数を割り算し、商と余りのペアを返す関数です。
pow(x, y)関数とは、数値のべき乗(xのy乗)を計算する関数です。
min()関数とは、引数の中で最小の値を返す関数です。
max()関数とは、引数の中で最大の値を返す関数です。
sum()関数とは、引数の合計を返す関数です。
'''