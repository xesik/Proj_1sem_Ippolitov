# Дан символ C и строки S, S0. Перед каждым вхождением символа C в строку S
# вставить строку S0.
sss = str(input("Введите строку: "))
single = str(input("Введите символ: "))
sss0 = str(input("Введите строку для вставки перед символом: "))
ctrlv = ""    # Cоздаем пустой строку sss
for i in range(len(sss)):    # Проход по строке sss
    if sss[i] == single:    # Если в строке находится элемент single, тогда перед ним ставится строка sss0
        ctrlv += sss0
        ctrlv += sss[i]
    else:
        ctrlv += sss[i]
print(ctrlv)
