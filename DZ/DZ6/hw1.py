# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии:
# an = a1 + (n-1) * d. Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

print("Подставьте значения в формулу a1 + (n-1) * d")
a = int(input("Введите a: "))
d = int(input("Введите d: "))
n = int(input("Введите n: "))

for i in range(n):
    an = a + i * d
    print(an)
