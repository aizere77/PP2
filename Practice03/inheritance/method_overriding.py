class Animal:
    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def sound(self):   # overriding
        return "Woof!"

d = Dog()
print(d.sound())   # Woof!


class Person:
    def info(self):
        return "I am a person"

class Student(Person):
    def info(self):
        base = super().info()
        return base + " and also a student"

s = Student()
print(s.info())  # I am a person and also a student


class Car:
    def __init__(self):
        self.type = "Generic car"

class Tesla(Car):
    def __init__(self):
        super().__init__()
        self.type = "Electric Tesla"

t = Tesla()
print(t.type)   # Electric Tesla


class Shape:
    def area(self):
        return 0

class Square(Shape):
    def area(self):
        return "Area = side * side"

print(Square().area())


class File:
    def open(self):
        print("Opening a regular file")

class ImageFile(File):
    def open(self):
        print("Opening an image viewer")

img = ImageFile()
img.open()   # Opening an image viewer
