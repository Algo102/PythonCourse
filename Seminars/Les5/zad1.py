# Напишите программу, которая на вход принимает два числа A и B, и возводит
# число А в целую степень B с помощью рекурсии.

def degree(a, b, c):
    if b != 0:
        c *= a
        b -= 1
    else:
        return c
    return degree(a, b, c)

# Другое решение


def stepen(a, b):
    if b == 0:
        return 1
    else:
        return a * stepen(a, b-1)


num1 = int(input("Введите число А "))
num2 = int(input("Введите число Б "))
c = 1  # Для первого решения

print(degree(num1, num2, c))  # Для первого решения

print(stepen(num1, num2))
