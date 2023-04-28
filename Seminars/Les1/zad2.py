# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.

# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

import math

n = int(input("Введите количество учеников в первом классе : "))
m = int(input("Введите количество учеников во втором классе : "))
o = int(input("Введите количество учеников в третьем классе : "))

s1 = math.ceil(n/2)
s2 = math.ceil(m/2)
s3 = math.ceil(o/2)

print("Минимаьно количество необходимых парт: ", s1 + s2 + s3)

# Другое решение
c1 = (n+1) // 2
c2 = (m+1) // 2
c3 = (o+1) // 2
print("Минимаьно количество необходимых парт: ", c1 + c2 + c3)