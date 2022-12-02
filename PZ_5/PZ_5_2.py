# Описать функцию AddLeftDigit(D, K), добавляющую к целому положительному
# числу K слева цифру D (D — входной параметр целого типа, лежащий в диапазоне
# 1-9, K — параметр целого типа, являющийся одновременно входным и выходным).
# С помощью этой функции последовательно добавить к данному числу K слева
# данные цифры D1 и D2, выводя результат каждого добавления.
import random


def addleftdigit(d):    # Функция добавления числа d к K
    global K
    K = str(d) + K


def main():    # Добавление чисел d1 и d2 (Функция только для исключения ошибки PEP 8)
    for i in range(2):
        d = random.randrange(0, 10)
        addleftdigit(d)
        print(f"Измененное K+D{i+1}: {K}")


K = str(random.randrange(1, 1000))    # Рандомное К
print(f"Изначальное K: {K}")
main()
