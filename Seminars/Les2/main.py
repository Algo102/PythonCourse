# for i in range(0, 5, 1):  # for i in range(5): то же самое, от 0 до 4 с шагом 1
#     print(i)


# i = 0
# while (i < 5):
#     print(i)
#     i += 1


stroka = "qwerty"
for el in stroka:
    #    print(el, end="\n")
    # не забываем что следующий принт будет с этой же строки
    print(el, end=" ")


# else в цикле отработает если не будет прерываний, то есть цикл отработает сам до конца
# i = 0
# while (i < 5):
#     n = int(input("Введите цифру"))
#     if n == 0:
#         print("Вы ввели 0")
#         break
#     i += 1
# else:
#     print("End!!")
