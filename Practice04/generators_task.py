#1. Create a generator that generates the squares of numbers up to some number N.
def square_generator(N):
    for i in range(N+1):
        yield i*i
    
print("Squares up to N:")
for num in square_generator(5):
    print(num)


#2. Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def even_generator(N):
    for i in range(N+1):
        if (i % 2 == 0):
            yield i
    
N = (int(input()))
print("Even numbers:")
print(", ".join(str(num) for num in even_generator(N)))


#3. Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def divisible_generator(N):
    for i in range(N+1):
        if (i % 3 == 0 and i % 4 == 0):
            yield i
    
print("Divisble by 3 and 4:")
for num in divisible_generator(100):
    print(num)


#4. Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def squares(a, b):
    for i in range(a, b+1):
        yield i*i
    
print("Squares up to N:")
for num in squares(5, 10):
    print(num)


#5. Implement a generator that returns all numbers from (n) down to 0.
def numbers_down(N):
    while N >= 0:
        yield N
        N -= 1

print("All numbers from N to 0(down)")
for num in numbers_down(10):
    print(num)