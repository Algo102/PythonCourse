# Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

n = int(input("Введите трехзначное число : "))
n3 = n % 10
n2 = int((n % 100-n3)/10)  # n2 = (n%10) // 10
n1 = n//100

print(f"Сумма чисел: {n1}, {n2} и {n3} равна: ", n1+n2+n3)


# другое решение
n = input()
print(int(n[0]) + int(n[1]) + int(n[2]))
