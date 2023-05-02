slovar = {'1': 'one', '2': 'two'}
print(slovar)

slovar['pr'] = 'hello'
print(slovar)

# # Пробегаемся и выводим ключи
# for item in slovar:
#     print(item)

# # Выводим ключи и значение
# for item in slovar:
#     print(item, slovar[item])

# # Или так правильнее
# for (key, value) in slovar.items():
#     print(key, value)

# # Меняем значение работая в цикле
# for (key, value) in slovar.items():
#     if key == '1':
#         slovar[key] = "111"
# print(slovar)


# Срезы у списков
spisok = [1, 2, 3, 4, 5, 6, 7]
spisok2 = spisok[:2] + spisok[6:]
print(spisok2)

spisok3 = spisok[::2] # третий параметр это шаг
print(spisok3)

spisok4 = spisok[::-1] # третий параметр это шаг, он может идти справа налево
print(spisok4)