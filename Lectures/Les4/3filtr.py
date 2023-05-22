# функция Фильтр - принимает на вход 2 значения, функцию и объект, и фильтр будет возвращать только те объекты, которым функция вернула значение true

# создадим список
data = [15, 65, 9, 36, 175]

# сделаем выборку тех чисел, которые заканчиваются на 5. Создадим новый список, к которму применяем фильтр
res = list(filter(lambda x: x % 10 == 5, data))
print(res)

#  если посмотреть на функцию которую писали ранее, то можно заметить, что это и есть расписанный filtr
# def where(f, col):
#     return [x for x in col if f(x)]
# list2 = [1, 2, 3, 5, 8, 15, 38]
# res = map(int, list2)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

# заменим where на встроенную filtr
list2 = [1, 2, 3, 5, 8, 15, 38]
res = map(int, list2)
res = filter(lambda x: x % 2 == 0, res)
res = list(map(lambda x: (x, x**2), res))
print(res)
