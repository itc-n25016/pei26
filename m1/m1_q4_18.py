phrase = 'PythonProgramming'
list_p = [] # 空のリストを作成
for p in phrase: # phraseの1文字ずつを繰り返しでチェック
    if p not in list_p: # チェック文字がlist_pにない場合
        list_p.append(p) # pをlist_pに追加する(append)する
print(list_p) # ['P', 'y', 't', 'h', 'o', 'n', 'r', 'g', 'a', 'm', 'i']
print(len(phrase) - len(list_p)) # phraseの長さ(17)引くlist_pの長さ(11)で6となる
"""
.append()について調べておきましよう
len()関数について調べておきましよう
"""