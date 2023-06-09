# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и
# получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый,
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

n = int(input("Введите номер автобусного билета (6 цифр) : "))
n6 = n % 10
n5 = int((n % 100 - n6) / 10)
n4 = n // 100 % 10
n3 = n // 1000 % 10
n2 = n // 10000 % 10
n1 = n // 100000

if n1+n2+n3 == n4+n5+n6:
    print(
        f"УРА!! Ваш билет с номером {n}, счастливый, можно кушать")
else:
    print('Oh no ((((')

# Другой вариант
n = input()
if int(n[0]) + int(n[1]) + int(n[2]) == int(n[3]) + int(n[4]) + int(n[5]):
    print('Yes')
else:
    print("No")
