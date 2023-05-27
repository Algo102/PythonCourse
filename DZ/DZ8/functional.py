# 55.  Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

# Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести фамилию, и Вы должны реализовать функционал для изменения и удаления данных

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Поиск по фамилии

# 1 - Интерфейс
# 2 - работа с файлом
# 3 - алгоритм

# 1 - добавление контакта
# 2 - вывод всех
# 3 - поиск по фамилии
# 4 - выход

def create(path):
    try:
        file = open(path, 'r')
    except IOError:
        print('Создан новый справочник -> phone_book.txt ')
        file = open(path, 'w')
    finally:
        file.close()

def add_cont(file_name, stroka):
    data = open(file_name, 'a')
    data.write(stroka + "\n")
    data.close()

def show_all(file_name):
    data = open(file_name, "r")
    for line in data:
        print(line[:-1])
    data.close()
 
def search(file_name, stroka):
    a = 0
    data = open(file_name, 'r')
    for line in data:
        if stroka in line:
            print(line[:-1])
            a = 123
    if a != 123:
        print("*** Такого контакта нет ***")
    data.close()

def cont_del(file_name, stroka):
    data = open(file_name, 'r')
    list1 = list()
    for line in data:
        if stroka in line:
            continue
        if line !="": 
            list1.append(line)
    data.close()

    list1 = list(filter(lambda x: x != "", list1))
    data = open(file_name, 'w')
    for line in list1:
        data.write(line)
    data.close()
    print("*** Контакт был удален ***")

def cont_change(file_name, stroka):
    data = open(file_name, 'r')
    list2 = list()
    for line in data:
        if stroka in line:
            new_stroka = input('Введите новое ФИО и телефон: ')
            list2.append(new_stroka + '\n')
            continue
        list2.append(line)
    data.close()

    list2 = list(filter(lambda x: x != "", list2))
    data = open(file_name, 'w')
    for line in list2:
        data.write(line)
    data.close()
    print("*** Контакт был изменен ***")
