# Создайте класс "Животное", который содержит информацию о виде и возрасте
# животного. Создайте классы "Собака" и "Кошка", которые наследуются от класса
# "Животное" и содержат информацию о породе.
class Animal:
    def __init__(self, types, age):
        self.types = types
        self.age = age


class Dog(Animal):   # создание класса с доступом с возможностью добавлять атрибуты родительского класса
    def __init__(self, types, age, poroda):
        super().__init__(types, age)
        self.poroda = poroda


class Cat(Animal):
    def __init__(self, types, age, poroda):
        super().__init__(types, age)
        self.poroda = poroda


lizard1 = Animal('Игуана', 15)
cat1 = Cat("Британец", 2, "Коты и кошки британской породы отличаются врожденным аристократизмом, спокойствием "
                          "и доброжелательностью.")
dog1 = Dog("Самоед", 1, "Самоeдская собaка - одна из древнейших пород собак.")

print(lizard1.__dict__)
print(cat1.__dict__)
print(dog1.__dict__)
