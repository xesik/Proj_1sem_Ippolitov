# Создайте класс «Счетчик», который имеет атрибут текущего значения и методы для
# инкремента и декремента значения.
class Chet:  # создание класса
    def __init__(self, a):
        self.a = a

    def plus(self, y=0):
        return self.a + y

    def minus(self, x=0):
        return self.a - x


primer = Chet(1)
print(primer.plus(100))
print(primer.minus(100))
