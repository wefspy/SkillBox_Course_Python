# Дан список из N чисел. Напишите программу, которая сортирует
# элементы списка по возрастанию и выводит их на экран.
# Дополнительный список использовать нельзя.
#
# Постарайтесь придумать и написать как можно более эффективный алгоритм сортировки.
#
# Пример:
# Изначальный список: [1, 4, –3, 0, 10]
# Отсортированный список: [–3, 0, 1, 4, 10]

def bubble_sort(arr):
    len_arr = len(arr)
    if len_arr == 1:
        return

    for i in range(0, len_arr - 1):
        for j in range(i + 1, len_arr):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr

array = input('Изначальный список (Введите элементы через пробел): ').split()
array = [int(item) for item in array]
print(bubble_sort(array))

