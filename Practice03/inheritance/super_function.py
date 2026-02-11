class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog barks")

d = Dog()
d.speak()


class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no

s = Student("Alice", 101)
print(s.name, s.roll_no)


class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def start(self):
        super().start()
        print("Car is ready to drive")

c = Car()
c.start()


class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        super().show()
        print("Class B")

class C(B):
    def show(self):
        super().show()
        print("Class C")

obj = C()
obj.show()


class Parent:
    value = 10

    @classmethod
    def show_value(cls):
        print(cls.value)

class Child(Parent):
    value = 20

    @classmethod
    def show_value(cls):
        super().show_value()
        print(cls.value)

Child.show_value()


