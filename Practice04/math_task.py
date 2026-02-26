import math
#1. Write a Python program to convert degree to radian.

degree = float(input("Input degree: "))
radian = math.radians(degree)
print("Output radian:", round(radian, 6))
print()


#2. Write a Python program to calculate the area of a trapezoid.
height = int(input("Height:"))
first_base = int(input("base, first value:"))
second_base = int(input("base, second value:"))
area = ((first_base + second_base) / 2) * height
print(area)


#3. Write a Python program to calculate the area of regular polygon.
n = int(input("Input number of sides: "))
length = float(input("Input the length of a side: "))

area_polygon = (n * length ** 2) / (4 * math.tan(math.pi / n))
print("The area of the polygon is:", int(area_polygon))
print()


#4. Write a Python program to calculate the area of a parallelogram.
base = float(input("Length of base: "))
height_par = float(input("Height of parallelogram: "))

area_parallelogram = base * height_par
print("Expected Output:", area_parallelogram)