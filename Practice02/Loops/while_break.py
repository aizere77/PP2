x = 1
while True:
    print(x)
    if x == 3:
        break
    x += 1


i = 10
while i >= 1:
    print(i)
    i -= 1


secret = 7
while True:
    guess = int(input("Guess the number: "))
    if guess == secret:
        print("Correct!")
        break
    print("Try again")


numbers = [3, 7, 2, 9, 5]
target = 9
i = 0
while i < len(numbers):
    if numbers[i] == target:
        print("Found at index", i)
        break
    i += 1


password = "1234"
user_input = ""

while user_input != password:
    user_input = input("Enter password: ")

print("Access granted")

