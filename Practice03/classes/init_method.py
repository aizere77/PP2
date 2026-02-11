class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alice")
print(p.name)


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

r = Rectangle(10, 5)
print(r.length, r.width)


class Student:
    def __init__(self, name, grade="A"):
        self.name = name
        self.grade = grade

s1 = Student("Bob")
s2 = Student("Emma", "B")


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance if balance >= 0 else 0

acc = BankAccount("Alice", -100)
print(acc.balance)  # 0


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = 3.14159 * radius * radius

c = Circle(5)
print(c.area)
