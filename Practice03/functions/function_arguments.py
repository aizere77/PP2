def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument


def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")


def add(a, b):
    return a + b

print(add(3, 5))


def greet(name, message):
    print(message, name)

greet(name="Alice", message="Hello")
greet(message="Hi", name="Bob")

