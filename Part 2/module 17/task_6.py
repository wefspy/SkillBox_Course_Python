# Часто в программировании приходится писать код исходя из результата,
# который требует заказчик. В этот раз ему нужно получить двумерный список:
#
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
#
# Напишите программу, которая генерирует такой список и выводит его на экран.
# Используйте только list comprehensions.

count_sub_arr = 4
count_elm_in_sub_arr = 3
diff_between_elm = 4

print([[elm for elm in range(num_sub_ar, num_sub_ar + count_elm_in_sub_arr * diff_between_elm, diff_between_elm)]
       for num_sub_ar in range(1, count_sub_arr + 1)])