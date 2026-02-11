def square(x):
    return x * x

result = square(4)
print(result)


def calculate(a, b):
    return a + b, a - b

sum_val, diff_val = calculate(10, 3)
print(sum_val, diff_val)


def greet(name):
    print("Hello", name)

result = greet("Alice")
print(result)   # None


def check_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even(7))


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
