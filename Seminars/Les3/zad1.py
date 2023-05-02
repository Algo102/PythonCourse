# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Input: [1, 2, 3, 1, 1, 5, 10, 20, 20, 30]

list_1 = []
n = int(input("Введите количество значений: "))

for i in range(n):
    m = int(input("Введите значение: "))
    list_1.append(m)
print(list_1)

# Первое решение
# c = set()
c = set(list_1.copy())
print(type(c))
print(c)
print("Уникальных элементов: ", len(c))

# Второе решение
# list_2 = []
# for i in list_1:
#     if (not i in list_2):
#         list_2.append(i)
# print(list_2)
# print(len(list_2))

# Третье решение
print(len(set(list_1)))
