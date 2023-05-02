# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5, 6, 7, 8, 9] k = 3
# Output: [7, 8, 9, 1, 2, 3, 4, 5, 6]

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_2 = list_1.copy()+list_1.copy()
list_3 = []

k = int(input("Введите смещение: "))

for i in range(len(list_1)):
    list_3.insert(i, list_2[i+(len(list_1)-k)])
print(list_3)

# Второе решение
print(list_2[len(list_1)-k:(len(list_1)-k)+len(list_1):1])

# Третье решение
print(list_1[len(list_1)-k:] + list_1[:len(list_1)-k:1])
# То же самое
print(list_1[-k:] + list_1[:-k:1])
