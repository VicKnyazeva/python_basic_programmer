# Вычислить число π c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141.$    10^{-1} ≤ d ≤10^{-10}

import math


def calc_pi(digits):
    if digits > 7:
        # при 7 достигается точность в 13 десятичных знаков после запятой!
        # дальше начинаются проблемы с ошибками округления при вычислениях
        digits = 7

    precision = 10 ** (-digits)
    n = 0
    S1 = 0  # верхняя граница
    S2 = 0  # нижняя граница
    while True:
        n += 1  # n становится нечётным
        S1 = S2 + 4 / (2 * n - 1)
        n += 1  # n становится чётным
        S2 = S1 - 4 / (2 * n - 1)
        delta = S1 - S2
        if delta <= precision:
            break;  # достигнута нужная точность!

    return ((S1 + S2) / 2, n // 2)


def calc_precision(diff):
    for d in range(1, 15):
        r = round(diff, d);
        if r != 0:
            return d;
    return d


digits = 5

print(f"math.pi : {math.pi:+.15f}")
print(f"точность: {digits}")

pi, iterations = calc_pi(digits)
print(f"Грегори : {pi:+.15f} (итераций: {iterations})")
diff = math.pi - pi
print(f"фактическая точность: {calc_precision(diff) - 1} цифр (ошибка: {diff:+.15f})")
