# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

def print_list(list):
    print(f"Исходный список: {list}")

def pairs_multiply(list):
    i = 0
    j = len(list) - 1
    new_list = []

    while (i <= j):
        ni = list[i]
        nj = list[j]
        new_list.append(ni * nj)

        i += 1
        j -= 1

    print(f"Произведение пар чисел: {new_list}", end=" ")

def task2_1(list):
    print("Test 1")
    list = [2, 3, 4, 5, 6]
    print_list(list)
    pairs_multiply(list)

    print("\n\nTest 2")
    list = [2, 3, 5, 6]
    print_list(list)
    pairs_multiply(list)

task2_1(list)