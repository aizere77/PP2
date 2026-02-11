class Student:
    school_name = "ABC School"   # class variable

s1 = Student()
s2 = Student()

print(s1.school_name)
print(s2.school_name)


class Car:
    wheels = 4

Car.wheels = 6   # change at class level

c1 = Car()
c2 = Car()

print(c1.wheels)
print(c2.wheels)


class Employee:
    company = "TechCorp"   # class variable

    def __init__(self, name):
        self.name = name  # instance variable

e1 = Employee("Alice")
e2 = Employee("Bob")

print(e1.company, e1.name)
print(e2.company, e2.name)


class User:
    count = 0

    def __init__(self):
        User.count += 1

u1 = User()
u2 = User()
u3 = User()

print(User.count)


class Product:
    tax_rate = 0.1

    @classmethod
    def change_tax(cls, new_rate):
        cls.tax_rate = new_rate

Product.change_tax(0.15)
print(Product.tax_rate)
