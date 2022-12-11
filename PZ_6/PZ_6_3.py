# Дано множество A из N точек (N > 2, точки заданы своими координатами x, у). Найти
# наименьший периметр треугольника, вершины которого принадлежат различным
# точкам множества A, и сами эти точки (точки выводятся в том же порядке, в котором
# они перечислены при задании множества A).
import math
tochki = []
for i in range(3):
    print("Введите координату x,y: ")    # Ввод координвт
    for n in range(2):
        tochki.append(int(input()))
R1 = math.sqrt(pow((tochki[2]-tochki[0]), 2) + pow((tochki[3]-tochki[1]), 2))    # |
R2 = math.sqrt(pow((tochki[4]-tochki[2]), 2) + pow((tochki[5]-tochki[3]), 2))    # | <-- Вычисление периметра
R3 = math.sqrt(pow((tochki[0]-tochki[4]), 2) + pow((tochki[1]-tochki[5]), 2))    # |
print(R1+R2+R3)
