# Посчитать факториал (произведение 1 до N) и треугольное число (сумма чисел от 1 до N) 
# для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов

def factor(n):
    if n == 1:
        return 1
    else:
        return factor(n-1) * n
    
def treug(n):
    if n == 1:
        return 1
    else:
        return treug(n-1) + n
print("Программа для нахождения факториала и треугольного числа")
numb = int(input('Введите число : '))
print("Факториал {0} равен {1} ".format(numb, factor(numb))) 
print("Треугольное число от {0} равен {1} ".format(numb, treug(numb)))