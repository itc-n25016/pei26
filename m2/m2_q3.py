list_a = [7.0, 9.0, 11, 14.0, 3, 4.0, 2] # 異なるtypeをリストに格納できる
list_b = [12, 1, 6.0, 3, 7]

print(list_a[1] * list_b[-2]) # 27.0
print(str(list_a[4] + int(list_b[2])) + '番') # 3+6 =　9番　←　最終的に文字列として扱われる
print(divmod(list_a[3], list_b[4])) # divmod(14.0, 7) = (2.0, 0.0)　←　14.0がfloatなので、結果もflaot

list_c = [2.05, 5] 
list_b += list_c # [12, 1, 6.0, 3, 7, 2.05, 5]

print(list_a[2] % list_b[4]) # 11 % 7 = 4
print(min(list_b[2:6])) # スライス指定で、min([6.0, 3, 7, 2.05])なので、2.05
print(round(list_c[0], list_b[1])) # round(2.05, 1)つまり、2.05の小数点　1桁までのこす（丸める）ので2.0
