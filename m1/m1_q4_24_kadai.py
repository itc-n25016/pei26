animals = ['Dog', 'Cat', 'Rabbit', 'Horse', 'Dolphin']
total = 0
for animal in animals:
    print(f'totalの値は{total}')
    from_D = animal.startswith('D') 
    is_long = len(animal) > 5 
    if from_D and is_long: 
        break 
    elif not from_D and is_long: 
        total += animal.find('b') 
    else:
        total += len(animal) 
print(total)
