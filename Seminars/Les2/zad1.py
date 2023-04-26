# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
# Input: 5
# Output: 120

# num = int(input("Введите число до которого будет рассчитан факториал : "))

# fact = 1
# while num > 1:
#     fact = fact * num
#     num -= 1
# print(fact)

# Для интересногот вывода
number = tempNumber = int(input(
    "Введите число до которого будет рассчитан факториал : "))
factorial = 1
while tempNumber != 1:
    factorial *= tempNumber
    tempNumber -= 1
print(f"Факториал {number} = {factorial}")


# другое решение
# n = int(input("Введите число до которого будет рассчитан факториал : "))

# res = 1
# i = 1
# while i > n:
#     res = res * i
#     i += 1
# print(res)
