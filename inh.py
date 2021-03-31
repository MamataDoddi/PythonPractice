class Animal():
    def __init__(self):
        print("Animal Created")
    def whoAmI(self):
        print("Animal")
    def eat(self):
        print("Eating")
class Dog(Animal):
    def __init__(self):
        print("Dog created")
    def eat(self):
        print("dog eating")
        #super().eat()

obj=Dog()
obj.eat()
obj.whoAmI()