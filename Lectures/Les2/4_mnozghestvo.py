# Уникальные элементы в хаотичном порядке

color = {'red', 'green', 'blue'}
print(color)
color.add('red')
print(color)  # ни чего не поменялось, т.к. ред уже есть
# добавлось на случайную позицию, но это нам и без разницы
color.add('grey')
print(color)
color.remove('red')  # Удаление значения
print(color)
# color.remove('red') # Ошибка, т.к. такого элемента нет
# Удаление элемента в случае его наличиия
color.discard('red')
color.clear()  # Удаление всех элементов
print(color)
q = set()  # Создание пустого множества
print(color)

# Операции со множествами
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()  # Копирование а в с
u = a.union(b)  # Объединение уникальных значений
i = a.intersection(b)  # Объединение схожих значений
# Вычитание из а множества, б. а-б
dl = a.difference(b)
# Вычитание из б множества, а. б-а
dr = b.difference(a)
# - сначала решаем скобки, а потом слева на право
q = a.union(b).difference(a.intersection(b))
print(q)

# Замороженнное множество
# Создали копию а, без возможности изменения
w = frozenset(a)
print(w)
