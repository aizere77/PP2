numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6]


numbers = [10, 15, 20, 25, 30]
odds = list(filter(lambda x: x % 2 != 0, numbers))
print(odds)  # [15, 25]


words = ["cat", "apple", "dog", "banana"]
long_words = list(filter(lambda x: len(x) > 4, words))
print(long_words)  # ['apple', 'banana']


nums = [-5, -2, 0, 3, 7, -1]
positive_nums = list(filter(lambda x: x > 0, nums))
print(positive_nums)  # [3, 7]


names = ["Alice", "Bob", "Annie", "Charlie"]
a_names = list(filter(lambda x: x.startswith("A"), names))
print(a_names)  # ['Alice', 'Annie']
