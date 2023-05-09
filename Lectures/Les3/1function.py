# 1 Нет раздичия функции или процедуры, в Питоне все функции
# 2 Пишется без типа данных
# 3 Сколько элементов передаем, столько и принимаем и наоборот
# 4 После ретурна функция прекращает работу

# программа суммирует числа от 1 до N

def sumNumbers(n):
    summ = 0
    for i in range(1, n+1):
        summ += i
    print(summ)
sumNumbers(5)

# ИЛИ ТАК
def sumNumbers1(n):
    summ = 0
    for i in range(1, n+1):
        summ += i
    return summ
print(sumNumbers1(5))

# ИЛИ ТАК
def sumNumbers2(n):
    summ = 0
    for i in range(1, n+1):
        summ += i
    return summ
a = sumNumbers2(5)
print(a)

# можно передавать аргументам, значения по умолчанию
def sumNumbers2(n, y = 'Hello'):
    print(y)
    summ = 0
    for i in range(1, n+1):
        summ += i
    return summ
a = sumNumbers2(5)
print(a)

# но если мы передадим какое либо значение, то оно будет в приоритете
def sumNumbers2(n, y = 'Hello'): # значение по умолчанию
    print(y)
    summ = 0
    for i in range(1, n+1):
        summ += i
    return summ
a = sumNumbers2(5, 'MESSAGE')
print(a)

# Для передачи, неопределенного количества аргументов, использум *
def sumStr(*args):
    res = ''
    for i in args:
        res += i
    return res
print(sumStr('q', 'e', 'l'))


# Вызываем функцию из файла
# import modul1 # Импортируем модуль
# #modul1.max1(5, 9) # обращаемся к этой функции
# print(modul1.max1(5, 9)) # Вызываем и сразу печатаем

# ИЛИ
from modul1 import max1
print(max1(5,9))

# Чтоб импортировать все функции из модуль1 нужно поставить *
from modul1 import *

# Чтоб каждый раз не писать длинное имя функции модуль1 можно сократить имя модудя для вызова в программе
import modul1 as m1
print(m1.max1(5, 9))