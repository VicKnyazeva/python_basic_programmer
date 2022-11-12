# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def task_2():
        try:
            N = int(input("Ведите число: "))
            initial_list = list([e for e in range(1, N+1)])
            result_list = []
            result_list = [result_list[-1] for x in range(1, N+1) if not result_list.append(x*result_list[-1] if result_list else 1)]
            print("Исходный список факториалов: ")
            print(result_list)

            # Демо работы zip
            zip_demo = list(zip(initial_list, result_list))
            print("\nСписок кортежей факториалов с индексами: ")
            print(zip_demo)
        except:
            print("Преобразование введенного числа не удалось")

task_2()