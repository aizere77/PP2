numbers = [5, 2, 9, 1, 7]
sorted_numbers = sorted(numbers, key=lambda x: x)
print(sorted_numbers)  # [1, 2, 5, 7, 9]


numbers = [-10, -3, 5, 2, -8]
sorted_by_abs = sorted(numbers, key=lambda x: abs(x))
print(sorted_by_abs)  # [2, -3, 5, -8, -10]


points = [(1, 3), (4, 1), (2, 2)]
sorted_points = sorted(points, key=lambda x: x[1])
print(sorted_points)  # [(4, 1), (2, 2), (1, 3)]


words = ["apple", "kiwi", "banana", "fig"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)  # ['fig', 'kiwi', 'apple', 'banana']


students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78}
]

sorted_students = sorted(students, key=lambda x: x["score"])
print(sorted_students)
