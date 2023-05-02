# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

spis = [0, -1, 5, 2, 3]

count = 0
for i in range(len(spis)-1):
    if spis[i+1] > spis[i]:
        count += 1
        print(spis[i+1], " > ", spis[i])
print(count)

# Или так
count = 0
for i in range(1, len(spis)):
    if spis[i-1] < spis[i]:
        count += 1
        print(spis[i], " > ", spis[i-1])
print(count)
