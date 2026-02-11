square = lambda x: x * x
print(square(5))  # 25


add = lambda a, b: a + b
print(add(3, 7))  # 10


max_value = lambda a, b: a if a > b else b
print(max_value(10, 7))  # 10


numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16]


numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4, 6]


points = [(1, 2), (3, 1), (5, 0)]
sorted_points = sorted(points, key=lambda p: p[1])
print(sorted_points)  # [(5, 0), (3, 1), (1, 2)]
