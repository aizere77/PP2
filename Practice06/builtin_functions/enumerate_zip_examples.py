names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]

# enumerate()
for i, name in enumerate(names):
    print(i, name)

# zip()
for name, score in zip(names, scores):
    print(name, score)

# Type checking & conversion
x = "123"
print(type(x))

num = int(x)
print(type(num))