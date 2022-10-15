#Реализуйте алгоритм перемешивания списка.
import random

def task_5():
    list = [1, 2, 3, 4, 5]
    print(f"Исходный список: {list}")

    for i in range(0, len(list)):
        j = random.randrange(0, len(list))
        list[i], list[j] = list[j], list[i]

    print(f"Перемешанный список: {list}")

task_5()