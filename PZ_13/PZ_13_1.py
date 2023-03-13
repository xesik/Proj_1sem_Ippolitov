from random import randint
a = []
for i in range(3):
    for n in range(3):
        a.append(randint(1, 20))
        if i == 2:
            a = [0, 0, 0]
    print(a)
    a = []
