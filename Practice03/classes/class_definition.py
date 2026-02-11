class Person:
    pass

p = Person()
print(p)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 25)
print(p.name)
print(p.age)


class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("Woof! My name is", self.name)

d = Dog("Buddy")
d.bark()


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

calc = Calculator()
print(calc.add(5, 3))
print(calc.subtract(10, 4))


class Student:
    def __init__(self, name, grade="A"):
        self.name = name
        self.grade = grade

s1 = Student("Bob")
s2 = Student("Emma", "B")

print(s1.name, s1.grade)
print(s2.name, s2.grade)
