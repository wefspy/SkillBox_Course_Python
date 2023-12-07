# Напишите функцию, которая сортирует по возрастанию кортеж, состоящий из целых чисел, и возвращает его отсортированным.
# Если хотя бы один элемент не является целым числом, то функция возвращает исходный кортеж.
#
# Основной код оставьте пустым или закомментированным (используйте его только для тестирования).
#
# Пример вызова функции:
# tpl = (6, 3, -1, 8, 4, 10, -5)
# print(tpl_sort(tpl))
# Ответ в консоли: (-5, -1, 3, 4, 6, 8, 10)

user_tuple = (6, 3, -1, 8, 4, 10, -5)


def sort_tuple(tpl):
    arr = list(tpl)
    for pointer in range(len(arr) - 1):
        for runner in range(pointer, len(arr)):
            if arr[runner] < arr[pointer]:
                arr[pointer], arr[runner] = arr[runner], arr[pointer]

    return tuple(arr)


print(sort_tuple(user_tuple))
