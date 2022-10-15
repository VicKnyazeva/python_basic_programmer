# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

def task_3():
    try:
        n = int(input("Ведите количество элементов последовательности: "))
        list = []
        for i in range(1, n+1):
            list.append((1 + 1/i) ** i)

        print("Последовательность:", end=" ")
        print(["{:4.3f}".format(i) for i in list])

        sum = 0
        for e in list:
            sum += e

        print("Сумма чисел последовательности: {:4.3f}".format(sum))
    except:
        print("Преобразование введенного числа не удалось")

task_3()