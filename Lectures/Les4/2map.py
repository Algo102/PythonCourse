# map - функция которая принимает на вход два аргумента, функцию и объект и применяет фунци. которую передаем ко всем элементам нашего объекта и его возвращает

# с помощью генератора списка заполним список
list1 = [x for x in range(1, 20)]
print(list1)

# list1 равен списку, в котором будем вызывать map и применять функцию, которую пишем через lambda. Из list1 берем элемент, который к которому прибавим 10 10
list1 = list(map(lambda x: x + 10, list1))
print(list1)


# ЗАДАЧА 
# C клавиатуры вводится некий набор чисел, в качестве разделителя используется пробел. Этот набор чисел будет считан в качестве строки. Как превратить list строк в list чисел?

# преобразование строки в спиcок
data = '15 156 96 3 5 8'
# print(data)
# data = data.split() # получаем раздельный список строк, но не чисел
# print(data)

# для получения чисел используем map
# сразу говорим, что это список, вызываем функцию  map, в которой к каждому объекту будем применять int, а объект это data.split
# Результатом работы map то итератор, который пробегается один раз
data = list(map(int, data.split()))
print(data)




# посмотрев на задачу, которую писали ранее, видно что функция select это и есть расписанная функция map, которая встроена в пайтон
# def select(f, col):  
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# list1 = [1, 2, 3, 5, 8, 15, 38]

# res = select(int, list1)
# print(res)

# res = where(lambda x: x % 2 == 0, res)
# print(res)

# res = select(lambda x: (x, x**2), res)
# print(res)

# и можно select заменить на map
def where(f, col):
    return [x for x in col if f(x)]

list2 = [1, 2, 3, 5, 8, 15, 38] 

res = map(int, list2)
print(res)

res = where(lambda x: x % 2 == 0, res)
print(res)

res = list(map(lambda x: (x, x**2), res))
print(res)
