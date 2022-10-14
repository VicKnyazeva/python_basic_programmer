# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math
import numpy as np


def task_5():
    print('====== Start Task 5 ======\n')

    try:
        x1 = float(input("Введите координату X первой точки: "))
        y1 = float(input("Введите координату Y первой точки: "))
        x2 = float(input("Введите координату X второй точки: "))
        y2 = float(input("Введите координату Y второ1 точки: "))

        calculate_distance(x1, y1, x2, y2)
        #numpy_version(x1,y1,x2,y2)
    except:
        print("Преобразование введенных значений не удалось")

    print('\n====== End Task 5 ========')

def calculate_distance(x1,y1,x2,y2):
    print(f"Евклидово расстояние {math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))}")

def numpy_version(x1,y1,x2,y2):
    point_1 = np.array((x1, y1))
    point_2 = np.array((x2, y2))
    square = np.square(point_1 - point_2)
    sum_square = np.sum(square)
    distance = np.sqrt(sum_square)

    print(f"Евклидово расстояние между указанными точками: {distance}")

task_5()