class A:
    def method_a(self):
        print("Method A")

class B:
    def method_b(self):
        print("Method B")

class C(A, B):
    pass

c = C()
c.method_a()  # Method A
c.method_b()  # Method B


class A:
    def greet(self):
        print("Hello from A")

class B:
    def greet(self):
        print("Hello from B")

class C(A, B):
    def greet(self):
        print("Hello from C")  # overrides both parents

c = C()
c.greet()  # Hello from C


class A:
    def show(self):
        print("A's show")

class B:
    def show(self):
        print("B's show")

class C(A, B):
    def show(self):
        super().show()  # follows Method Resolution Order (MRO)

c = C()
c.show()  # A's show


class A:
    def __init__(self):
        print("Init A")

class B:
    def __init__(self):
        print("Init B")

class C(A, B):
    def __init__(self):
        super().__init__()  # calls A's __init__ because of MRO
        print("Init C")

c = C()


class Flyer:
    def fly(self):
        print("Can fly")

class Swimmer:
    def swim(self):
        print("Can swim")

class Duck(Flyer, Swimmer):
    def quack(self):
        print("Quack!")

d = Duck()
d.fly()   # Can fly
d.swim()  # Can swim
d.quack() # Quack!
