num = 12
list_s = [] # からのリスト
s = 2 # ↓のコメントは1回目のループでの処理イメージ
while s <= num: # 2 <= 12はTrue
    if num % s == 0: # 12 % 2 == 0はTrue
        num //= s # //=は整数除算(切り捨て除算)して代入、つまり 12 // 2 = 6←これがnumに代入される
        if s not in list_s: # sはlist_sにないのでTrue
            list_s.append(s) # [2]となる
    else: # 1回目のループでは実行されない
        s += 1
print(list_s)

"""計算欄
1回目のループ後: num=6 list_s=[2] s=2
2回目のループ後: num=3 list_s=[2] s=2
3回目のループ後: num=3 list_s=[2] s=3
4回目のループ後: num=1 list_s=[2, 3] s=3
while 3 <= 1はFalseなのでループ終了
よって答えは[2, 3]となる"""