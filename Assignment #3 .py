
#  Q1 Write a program that calculates the sum, difference, product, and average of three numbers

a = 2
b = 4
c = 6

print("Sum =", a + b + c)
print("Difference =", a - b - c)
print("Product =", a * b * c)
print("Average =", (a + b + c) / 3)

#  Q2 Write Python code to calculate the area of the following shapes.
#  Area of triangle, square, circle and rectangle



# Triangle
base = 10
height = 12
triangle_area = 0.5 * base * height
print("Area of Triangle =", triangle_area)

# Square
side = 15
square_area = side * side
print("Area of Square =", square_area)

# Circle
radius = 16
π = 3.142
circle_area = π * radius * radius
print("Area of Circle =", circle_area)

# Rectangle
length = 10
width = 4
rectangle_area = length * width
print("Area of Rectangle =", rectangle_area)

# Q3 Write a program to swap values of two variables.

a = 8
b = 10

print(" Before Swapping ")
print("a =", a)
print("b =", b)

# Swapping using addition and subtraction
a = a + b
b = a - b
a = a - b

print(" After Swapping ")
print("a =", a)
print("b =", b)
