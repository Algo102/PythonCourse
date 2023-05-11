# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных строках.
# Ввод: 1 2 3 2 3
# Вывод: 2

import random

list1 = list()
num1 = int(input("Введите длину первого массива "))

for i in range(num1):
    list1.append(random.randint(0, 10))
print(list1)

count = 0

for i in range(len(list1)):
    for j in range(i + 1, len(list1)):
        if list1[j] == list1[i]:
            print(list1[j], " ", end=' ')
            count += 1

# Или так
# for i in range(len(list1)-1):
#     j = i + 1
#     while j < len(list1):
#         if list1[j] == list1[i]:
#             print(list1[j], " ", end=' ')
#             count += 1
#         j += 1

print(" ")
print("----------------------")
print("Количество повторений ", count)

