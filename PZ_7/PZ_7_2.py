# Дана строка, содержащая по крайней мере один символ пробела. Вывести подстроку,
# расположенную между первым и последним пробелом исходной строки. Если
# строка содержит только один пробел, то вывести пустую строку.
stroka = str(input("Введите строку: "))
indexes = []
ch = " "
for i in range(len(stroka)):    # Поиск пробелов в строке
    if stroka[i] == ch:
        indexes.append(i)
if len(indexes) >= 2:    # Исключение ошибки при нахождении менее 2 пробелов
    print(stroka[indexes[0]:indexes[-1]])
else:
    print(" ")
