list_a = ['Yokohama', 'Osaka', 'Nagoya', 'Sapporo', 'Fukuoka']
list_b = []
list_c = []
list_d = []
for name in list_a:
    if len(name) > 6:
        list_b.append(name)
    elif name.count('a') >= 1:
        list_c.append(name)
    else:
        list_d.append(name)
print(list_c)