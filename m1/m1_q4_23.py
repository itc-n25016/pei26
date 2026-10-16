ip_address = '192.168.3.1'
ip_spl = ip_address.split('.') # ['192', '168', '3', '1']
bin_exp = ''
for num in ip_spl:
    bin_exp += bin(int(num))[2:] + '.'
print(bin_exp[:-1]) # 11000000.10101000.11.1
print(type(bin_exp)) # <class 'str'>

'''メモ
splitメソッドは引数で指定された文字で分割し、リストを作る
bin関数とは整数を2進数に変換する関数です。
int関数とは文字列を整数に変換する関数です。

スライスについて[2:]はインデックス2以降を取得する
スライスについて[:-1]は末尾の1文字を除いて取得する
'''