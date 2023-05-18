
my_dict = { 'Khan': 4, 'Ali': 2, 'Luna': 6, 'Mark': 11, 'Pooja': 8, 'Sara': 1}

for key, value in my_dict.items():
    if key == 'Ali':
        my_dict[key] = 10

print(my_dict)