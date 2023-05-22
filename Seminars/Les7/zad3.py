# Программа должна принимать вещественные числа и выдавать сумму цифр
# 1,23 --> 6

digit = input("Enter number  ")
# замена точки на пустое место
digit = digit.replace('.', '').replace(',', '')
# digit = digit.replace(',', '')
print(digit)  # Еще стринговый
# sum - сумма цифр. Предварительно переводим в инт
# res = sum(map(lambda x: int(x), digit))  # sum - сумма цифр
res = sum(map(int, digit))  # а так проще и правельнее
print(res)
