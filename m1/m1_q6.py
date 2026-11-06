# ひらがな1文字を受け取り、hiragana_hyou内の位置を(横、縦)のタプルで返す関数
# (横、縦) = (外側リストのインデックス、内側リストのインデックス) 例：'い' → (0, 1)
# 見つからない場合はNoneを返す
def search_kana_idx(kana):
    idx_1 = 0 # 横(外側リスト)のインデックスを数えるカウンタ
    for gyou in hiragana_hyou:
        idx_2 = 0 # 縦(内側リスト)のインデックスを数えるカウンタ
        for ka in gyou:
            if ka == kana:
                return (idx_1, idx_2) # 見つかったら(横、縦)のタプルを返して終了する
            else:
                idx_2 += 1 # 内側のループなので、縦のカウンタを進める
        idx_1 += 1 # 外側のループなので、横のカウンタを進める
    return None # 文字が見つからない場合はNoneを返す

# グローバル変数の設定
hiragana_hyou = [['あ', 'い', 'う', 'え', 'お'],
                 ['か', 'き', 'く', 'け', 'こ'],
                 ['さ', 'し', 'す', 'せ', 'そ'],
                 ['た', 'ち', 'つ', 'て', 'と'],
                 ['な', 'に', 'ぬ', 'ね', 'の'],
                 ['は', 'ひ', 'ふ', 'へ', 'ほ'],
                 ['ま', 'み', 'む', 'め', 'も'],
                 ['や', '゛', 'ゆ', '゜', 'よ'],
                 ['ら', 'り', 'る', 'れ', 'ろ'],
                 ['わ', 'っ', 'を', 'ー', 'ん']]

print(hiragana_hyou)
hirabun = input('ひらがなの文を入力してください:')
codes = '' # (2)変換結果(インデックスを並べた暗号)を入れる文字列。初期値は空
for kana in hirabun: # 一文字ずつチェック
    idxs = search_kana_idx(kana) # idxsは(行、段)のタプル。見つからなければ None
    codes += '?' if idxs is None else f'{idxs[0]}{idxs[1]}' # 別欄(↓)で説明
print(codes)

ango = input('暗号を入力してください:')
kanas = ''
if len(ango) % 2 == 0: # 文字列の長さが偶数ならTrue(2文字で1組のため)
    for i in range(len(ango) // 2): # angoは2文字でかな1文字なので、組の数だけ繰り返す
        index_1 = int(ango[2 * i]) # 2*i 番目の文字を整数にする(行のインデックス)
        index_2 = int(ango[2 * i + 1]) # 2*i+1 番目の文字を整数にする(段のインデックス)
        kanas += '?' if hiragana_hyou[index_1][index_2] == '' else hiragana_hyou[index_1][index_2] # 別欄(↓)で説明
    print(kanas)
else:
    print('暗号の文字数は偶数でなければなりません')

'''補足欄
・条件式（三項演算子）について
codes += '?' if idxs is None else f'{idxs[0]}{idxs[1]}'
この処理は、以下のif/else文と同じ処理です。関連して抑えておきましょう。
if idxs is None: # idxsがNoneなら
    codes += '?' # '?' を連結する
else:
    codes += f'{idxs[0]}{idxs[1]}' # idxs[0]とidxs[1]を文字列にして、続けてcodeに連結する

kanas += '?' if index_2 > 4 else hiragana_hyou[index_1][index_2]
について
index_2は内側のリストのインデックスで、有効なのは0から4まで。
index_2が5以上だと範囲外になりエラーとなるので、その場合は'？'を連結する
このときelse側のhiragana_hyou[index_1][index_2]は表示されないのでエラーにならない。
(index_1は1桁の数字なので0〜9で、リストの行数10に収まる。そのため確認は不要)
'''