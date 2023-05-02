# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: ["V": "S001", "V": "S002", "VI": "S001", "VI": "S005", "VII": " S005 ",
# " V ":" S009 ", " VIII":" S007 "]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

dic = {"V": "S001", "V": "S002", "VI": "S001", "VI": "S005",
       "VII": "S005", " V ": " S009 ", " VIII": " S007 "}

list_1 = list()
for i in dic:
    list_1.append(dic[i])

# print(list_1)
print(set(list_1))


# А так еще оптимальнее
mnogh = set()
for i in dic:
    mnogh.add(dic[i])

print(mnogh)

# Или
mnogh2 = set()
for i in dic.values():
    mnogh2.add(i)

print(sorted(mnogh2))
