import math


# ex_1
x = int(input("Input degree: "))
print(f"Output radian: {math.radians(x)}\n\n")


# ex_2
height = int(input("Height: "))
a = int(input("Base, first value: "))
b = int(input("Base, second value: "))
print(f"Expected Output: {(a + b) / 2 * height}\n\n")


# ex_3
sides = int(input("Input number of sides: "))
if sides > 2:
    length = int(input("Input the length of a side: "))
    radius = length / (2 * math.tan(math.pi / sides))
    print(f"The area of the polygon is: {int(length * sides * radius / 2)}")
else:
    print("Such a polygon doesn't exist!")
print("\n\n")


# ex_4
length_of_base = int(input("Length of base: "))
height_of_par = int(input("Height of parallelogram: "))
print(f"Expected Output: {float(length_of_base * height_of_par)}")
