# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


def sum_elements(initial_list):
    print('Исходный список:')
    print(list(enumerate(initial_list, 1)))

    print('\nСписок элементов на нечётных позициях:')
    res_list = [x for i, x in enumerate(initial_list, 1) if i % 2 == 0]
    print(list(enumerate(res_list)))

    print(f"\nСумма элементов на нечётных позициях: {sum(res_list)} ")


some_list = [2, 3, 5, 9, 3]
sum_elements(some_list)