class Student:
    school_name = "ABC School"

    @classmethod
    def get_school_name(cls):
        return cls.school_name

print(Student.get_school_name())


class Student:
    school_name = "ABC School"

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

Student.change_school("XYZ School")
print(Student.school_name)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name, 2025 - birth_year)

p = Person.from_birth_year("Alice", 2000)
print(p.name, p.age)


class Car:
    count = 0

    def __init__(self, brand):
        self.brand = brand
        Car.count += 1

    @classmethod
    def total_cars(cls):
        return cls.count

Car("Toyota")
Car("Honda")
print(Car.total_cars())


class Animal:
    species = "Unknown"

    @classmethod
    def get_species(cls):
        return cls.species

class Dog(Animal):
    species = "Dog"

print(Dog.get_species())


