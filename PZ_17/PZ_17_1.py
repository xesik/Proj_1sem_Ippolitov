# -*- coding: utf-8 -*-
# Создайте класс «Счетчик», который имеет атрибут текущего значения и методы для
# инкремента и декремента значения.
class Chet:  # создание класса
    def __init__(self, balance):
        self.balance = balance

    def plus(self, y=0):
        return self.balance + y

    def minus(self, x=0):
        return self.balance - x


primer = Chet(1)
print(primer.__dict__)
print(primer.plus(100))
print(primer.minus(100))
