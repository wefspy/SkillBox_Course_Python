# Даны три списка.
# array_1 = [1, 5, 10, 20, 40, 80, 100]
# array_2 = [6, 7, 20, 80, 100]
# array_3 = [3, 4, 15, 20, 30, 70, 80, 120]
#
# Нужно выполнить две задачи:
#     найти элементы, которые есть в каждом списке;
#     найти элементы из первого списка, которых нет во втором и третьем списках.
#
# Каждую задачу нужно выполнить двумя способами:
#     без использования множеств;
#     с использованием множеств.

array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

print('Без использования множеств')
common_elms = []
for elm in array_1:
    if elm in array_2 and elm in array_3:
        common_elms.append(elm)
print(common_elms)

unique_elms = []
for elm in array_1:
    if elm not in array_2 and elm not in array_3:
        unique_elms.append(elm)
print(unique_elms)


print('С использованием множеств')
common_elms = set(array_1) & set(array_2) & set(array_3)
print(common_elms)

unique_elms = set(array_1) - set(array_2) - set(array_3)
print(unique_elms)