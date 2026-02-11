class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    pass

d = Dog()
d.speak()


class Animal:
    def eat(self):
        print("Eating...")

class Cat(Animal):
    def meow(self):
        print("Meow!")

c = Cat()
c.eat()
c.meow()


class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Bark!")

d = Dog()
d.speak()


class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

d = Dog("Buddy", "Labrador")
print(d.name, d.breed)


class Animal:
    pass

class Dog(Animal):
    pass

d = Dog()

print(isinstance(d, Dog))      # True
print(isinstance(d, Animal))   # True
print(issubclass(Dog, Animal)) # True
