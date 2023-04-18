# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
#     1 2 3 4 5
#     3
#     -> 1
# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
#     1 2 3 4 5
#     6
#     -> 5

import random

size_list = abs(int(input('Введите размер списка: ')))
user_number = int(input('Введите число которое хотите найти: '))

MIN_VAL_LIST = 0
MAX_VAL_LIST = 50

user_list = [random.randint(MIN_VAL_LIST, MAX_VAL_LIST) for _ in range(size_list)]
count = 0
difference = MAX_VAL_LIST
difference_number = 0



print(user_list)

for i in user_list:
    if i == user_number:
        count += 1

if count != 0:
    print(f'Заданное число {user_number} встречается {count} раз. ')
else:
    while count < size_list - 1:
        difference_temp = abs(user_number - user_list[count])
        if difference_temp < difference:
            difference = difference_temp
            difference_number = user_list[count]
        count += 1
    print(f'Ближайшее число к заданному это -> {difference_number}')



