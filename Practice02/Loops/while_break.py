x = 1
while True:
    print(x)
    if x == 3:
        break
    x += 1



while True:
    x = int(input())
    if x > 0:
        break


while True:
    n = int(input())
    if n == 0:
        break
    print(n)

    
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




