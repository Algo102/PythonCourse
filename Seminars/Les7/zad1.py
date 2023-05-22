# Вводится список целых чисел через пробел, Необходимо в нем оставить толькодвузначные числа. Использовать функцию фильтр

list1 = list(map(int, input("Введите цифры через пробел  ").split()))
print(list1)

res_list1 = list(filter(lambda x: 9 < abs(x) < 100, list1))
print(res_list1)
