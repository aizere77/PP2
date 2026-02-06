fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
  print(x)

for i in range(1, 6):
    print(i)


for i in range(10):
    if i % 2 == 0:
        print(i)

n = int(input())
total = 0

for i in range(1, n + 1):
    total += i

print(total)

s = input()

for i in range(len(s) - 1, -1, -1):
    print(s[i], end="")


numbers = [3, 5, 7, 9]

for n in numbers:
    print(n)


#Using the range() function:
for x in range(6):
  print(x)