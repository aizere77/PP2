def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add_numbers(1, 2, 3))    # 6
print(add_numbers(4, 5))       # 9


def greet(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}!")

greet("Hello", "Alice", "Bob")


def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Alice", age=25, city="Paris")


def greet_person(message, **person):
    print(message, person.get("name", "Guest"))
    print("Age:", person.get("age", "Unknown"))

greet_person("Hello", name="Bob", age=30)


def example(a, b, *args, c=10, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("c:", c)
    print("kwargs:", kwargs)

example(1, 2, 3, 4, c=20, x=100, y=200)
