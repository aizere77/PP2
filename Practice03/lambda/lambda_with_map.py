numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25]


nums = [10, 20, 30]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)  # [20, 40, 60]


words = ["apple", "banana", "cherry"]
upper_words = list(map(lambda x: x.upper(), words))
print(upper_words)  # ['APPLE', 'BANANA', 'CHERRY']


names = ["Alice", "Bob", "Charlie"]
first_letters = list(map(lambda x: x[0], names))
print(first_letters)  # ['A', 'B', 'C']


a = [1, 2, 3]
b = [4, 5, 6]
summed = list(map(lambda x, y: x + y, a, b))
print(summed)  # [5, 7, 9]
