# Дано целое число N (> 0).
# Найти сумму N2 + (N + 1)2 + (N + 2)2 + ... + (2N)2
put = input("Введите положительное число: ")
while type(put) != int:    # Обработка исключений
    try:
        put = int(put)
    except ValueError:
        print("Вы ввели неправильное число")
        put = input("Введите положительное число: ")
if put > 0:
    x = put**2    # Вычисление выражения
    s = 0
    while s in range(put):
        s += 1
        x = x + ((put + s) ** 2)
    print(f"Ответ: {x}")
else:
    print("Вы ввели отрицательное число")
