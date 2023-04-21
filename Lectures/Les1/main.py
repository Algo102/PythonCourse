# print(5, 8, 6)

# '''
# n = 1, 89
# print(n)
# print(type(n))
# '''

# n = 1.89
# print(n)
# print(type(n))

# """
# n = "He\'llo"
# print(n)
# print(type(n))
# """


# n = 'Ho"l"a'
# print(n)

# a = 5
# b = 5.63
# c = "Hello"

# print(a, b, c)
# print(a, ' - ', b, ' - ', c)
# print(f"{a} - {b} - {c}")
# print("{} - {} - {}".format(a, b, c))


# print("Enter first number")
# # Без инт будет соединение символов, а не сложение
# d = int(input())

# # ввод в той же строке
# e = int(input('Введите второе число - '))
# print(d, ' + ', e, ' = ', d + e)


# f = 5.364
# g = 4.3145
# print(round(a*b, 2))


# a = 1 > 4
# print(a, "1 > 4")

# a = 1 < 4 and 5 > 2
# print(a, "1 < 4 and 5 > 2")

# a = 1 == 2
# print(a, "1 == 2")

# a = 1 != 2
# print(a, "1 != 2")

# a = 'qwe'
# b = 'qwe'
# print(a == b, a, " = ", b)

# a = 1 < 3 < 5 < 10
# print(a, '1 < 3 < 5 < 10')



# username = input('Enter name: ')
# if username == 'Masha':
#   print('Ура ты вернулась Маша!')
# elif username == "Marina":
#   print('Я вас ждал Марина!!!')
# elif username == 'Ilnar':
#   print('Ильнар УРА!!!')
# else:
#   print('Привет: ', username)



# i = 0
# while i < 5:
#     # if i == 3:
#     #     break
#     i +=1
# else:
#     print('End!!!')
# print(i)

# break лучше не использовать, а использовать схему с флагом
# Программа ищем наименьший делитель
# n = int(input())
# flag = True
# i = 2
# while flag: # можно было написать flag == True
#     if n % i == 0: # если остаток от деления равен 0
#         flag = False
#         print(i)
#     elif i > n //2: # проверяем, введеное чило разделенное на 2, больше делителя
#         print(n)
#         flag = False
#     i +=1


# for i in 1, -2, 3, 0, 14:
#     print(i)

# r = range(5) # 0 1 2 3 4
# r = range(2, 5) # 2 3 4
# r = range(0, -5) # -------
# r = range(1, 10, 2) # 1 3 5 7 9
# r = range(100, 0, -20) # 100 80 60 40 20

# for i in r:
#     print(i)

# for i in 'qwerty':
#     print(i)

# a = 'qwerty'
# print(a[2])
# for i in a:
#     print(i)


# line = ''
# for i in range(5):
#     line = ''
#     for j in range(5):
#         line += '*'
#     print(line)

text = 'СъеШЬ ещё этих МяГкиХ французких булочек'
# print(len(text))
# print('ещё' in text)
# print(text.lower())
# print(text.upper())
# print(text.replace('ещё', 'ЕЩЁ'))
# print(text[0])
# print(text[len(text)-1])
# print(text[-1])
# print(text[-5])
# print(text[:])
# print(text[:2])
# print(text[20:])
# print(text[len(text)-2:])
print(text[2:9])
print(text[6:-18])
print(text[0:len(text):6])
print(text[::6])
print(text[2:9] + text[-5] + text[:2] )