from functional import *
from interface import interface

path = "phone_book.txt"
create(path)

enter = 99
while enter != 0:
    enter = interface()
    if enter == 1:
        stroka = str(input("Введите ФИО и номер телефона через пробел "))
        add_cont(path, stroka)
    elif enter == 2:
        print(show_all(path))
    elif enter == 3:
        stroka = str(input("Введите фамилию "))
        search(path, stroka)
    elif enter == 4:
        stroka = str(input("Введите фамилию для удаления "))
        cont_del(path, stroka)
    elif enter == 5:
        stroka = str(input("Введите фамилию для изменения "))
        cont_change(path, stroka)
print("Спасибо за работу")

