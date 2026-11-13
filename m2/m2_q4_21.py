list_a = [4, 8, 3, 7, 9]
list_b = [10, 3, 6, 7, 2]
list_c = []
i = 0
while i < 5: # i < 5より、0から4までの5回繰り返す(i+=1で増える)
    if list_a[i] > list_b[i]: 
        list_c.append(list_a[i] - list_b[i] ** 2) 
    elif list_a[i] < list_b[i]: 
        list_c.append(list_a[i] * 2 % 4) 
    else: 
        list_c.append((list_b[i] - list_a[i]) // 2) 
    i += 1 
print(max(list_c)) # 最大値

'''計算欄
4と10: (4 - 10) // 2 = -3
8と3 : 8 - 3 ** 2 = -1
3と6 : (6 - 3) // 2 = 1
7と7 : 7 * 2 % 4 = 2
9と2 : 9 - 2 ** 2 = 5
なのでmax([-3, -1, 1, 2, 5]) = 5

算術演算子と優先順位
**: べき乗。3 ** 2 = 9
 %: 余り。 14 % 4 = 2
//: 商の小数点以下切り捨て。3 // 2 = 1
※優先順位も気をつけましょう
**が最優先
'''