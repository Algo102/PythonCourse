# Дан список, вывести отдельно буквы и цифры
# [12, 'sadf', 5643] --> ['sadf'], [12, 5643]

list1 = [12, 'sadf', 5643]
res1 = list(filter(lambda x: type(x) == int, list1))
res2 = list(filter(lambda x: type(x) != int, list1))
print(res1, res2)
