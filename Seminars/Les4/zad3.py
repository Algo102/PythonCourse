# Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить значение наибольшего элемента
# последовательности, которая завершается первым встретившимся нулем (число 0 не входит в
# последовательность)”.

numbers = max = int(input("Введите цифру "))
# max = numbers

while (numbers != 0):
    # if (numbers > max):
    #     max = numbers
    max = numbers if numbers > max else max
    numbers = int(input("Введите цифру "))

# If можно записать тернанрным оператором, слева от if в случае true, после else присваивается в случае false
# (max = значение - false) if (условие) else (значение - false)
# max = numbers if numbers > max else max
# работать можно не тоько с цифрами, можно и со строками

print("Максимальная цифра ", max)
