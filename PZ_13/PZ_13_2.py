# В матрице элементы столбца N (N задать с клавиатуры) увеличить в два раза.
from random import randint
a = []
s = int(input("Выберите столбец от 1 до 3 --> "))
s -= 1
for i in range(3):
    for n in range(3):
        a.append(randint(1, 20))
    a[s] *= 2
    print(a)
    a = []
