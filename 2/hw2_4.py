# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

def task_4():
    try:
        N = int(input("Ведите количество элементов списка: "))

        list = []
        for e in range(-N, N + 1):
            list.append(e)

        with open('file.txt', 'r') as indexes:
            data = indexes.read()

        product = 1
        for i in data.split(' '):
            index = int(i)
            if (0 <= index and index < len(list)):
                product *= list[index]

        #print(list)
        print(f"Произведение элементов: {product}")
    except:
        print("Преобразование введенного числа не удалось")

task_4()

