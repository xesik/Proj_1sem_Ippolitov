# С начала суток прошло N секунд (N — целое).
# Найти количество
# полных минут, прошедших с начала последнего часа.
seconds = int(input("Введите целое число: "))
while type(seconds) != int:  # Обработка исключений
    try:
        seconds = int(seconds)
    except ValueError:
        print("Вы ввели неправильное число")
        seconds = int(input("Введите целое число: "))
seconds = seconds / 60    # Вычисление полных минут
minutes = int(seconds % 60)
print(f"Количество полных минут: {minutes}")
