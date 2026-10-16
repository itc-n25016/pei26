animals = ['Dog', 'Cat', 'Rabbit', 'Horse', 'Dolphin']
total = 0
for animal in animals:
    from_D = animal.startswith('D') 
    is_long = len(animal) > 5 # 5文字より多ければTrue、そうでなければFalseを返す
    if from_D and is_long: # どちらもTrueの場合
        break # ループ終了
    elif not from_D and is_long: # from_DがFalseかつ、is_longがTrue
        total += animal.find('b') 
    else:
        total += len(animal) # animalの文字列をtotalに足し込む
print(total)

'''計算欄
startswith('D')メソッドについて、今回は
'D'で始まっていたらTrue、そうでなければFalseを返す
find('b')メソッドについて、bが最初に見つかったインデックスを返す。見つからなければ-1を返す

animal from_D is_long 処理
'Dog' True False total += len(animal) 3
'Cat' False False total += len(animal) 3
'Rabbit' False True total += animal.find('b') インデックスを返すので2
'Horse' False False total += len(animal) 5
'Dolphin' True True break 

よって、0+3+3+2+5=13
'''