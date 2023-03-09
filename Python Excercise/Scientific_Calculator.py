import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def exponent(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error: Square root of a negative number"
    return math.sqrt(x)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def arcsine(x):
    return math.degrees(math.asin(x))

def arccosine(x):
    return math.degrees(math.acos(x))

def arctangent(x):
    return math.degrees(math.atan(x))

def area_of_circle(radius):
    return math.pi * radius ** 2

def circumference_of_circle(radius):
    return 2 * math.pi * radius

def area_of_triangle(base, height):
    return 0.5 * base * height

def area_of_rectangle(length, width):
    return length * width

def area_of_square(side):
    return side ** 2
while True:
    print("\n\n")
    print(" |********************************* |")
    print(" |                                  |")
    print(" |***** Scientific Calculator ***** |")
    print(" |                                  |")
    print(" |********************************* |")
    print(" |***** 1. Addition *************** |")
    print(" |***** 2. Subtraction ************ |")
    print(" |***** 3. Multiplication ********* |")
    print(" |***** 4. Division *************** |")
    print(" |***** 5. Exponentiation********** |")
    print(" |***** 6. Square Root ************ |")
    print(" |***** 7. Sine ******************* |")
    print(" |***** 8. Cosine ***************** |")
    print(" |***** 9. Tangent **************** |")
    print(" |***** 10. Arcsine *************** |")
    print(" |***** 11. Arccosine ************* |")
    print(" |***** 12. Arctangent ************ |")
    print(" |***** 13. Area of Circle ******** |")
    print(" |***** 14. Circumference of Circle |")
    print(" |***** 15. Area of Triangle ****** |")
    print(" |***** 16. Area of Rectangle ***** |")
    print(" |***** 17. Area of Square ******** |")
    print(" |***** 18. Quit ****************** |")
    print(" |********************************* |")
    
    choice = int(input("Enter your choice (1-18): "))

    if choice in (1, 2, 3, 4, 5):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    if choice == 1:
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == 2:
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == 3:
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == 4:
        print(num1, "/", num2, "=", divide(num1, num2))

    elif choice == 5:
        print(num1, "^", num2, "=", exponent(num1, num2))

    elif choice == 6:
        num = float(input("Enter a number: "))
        print("sqrt(", num, ")=", square_root(num))

    elif choice == 7:
        angle = float(input("Enter an angle in degrees: "))
        print("sin(", angle, ")=", sine(angle))

    elif choice == 8:
        angle = float(input("Enter an angle in degrees: "))
        print("cos(", angle, ")=", cosine(angle))

    elif choice == 9:
        angle = float(input("Enter an angle in degrees: "))
        print("tan(", angle, ")=", tangent(angle))

    elif choice == 10:
        x = float(input("Enter a value between -1 and 1: "))
        print("arcsin(", x, ")=", arcsine(x))

    elif choice == 11:
        x = float(input("Enter a value between -1 and 1: "))
        print("arccos(", x, ")=", arccosine(x))

    elif choice == 12:
        x = float(input("Enter a value: "))
        print("arctan(", x, ")=", arctangent(x))

    elif choice == 13:
        radius = float(input("Enter the radius of the circle: "))
        print("Area of the circle with radius", radius, "=", area_of_circle(radius))

    elif choice == 14:
        radius = float(input("Enter the radius of the circle: "))
        print("Circumference of the circle with radius", radius, "=", circumference_of_circle(radius))

    elif choice == 15:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        print("Area of the triangle with base", base, "and height", height, "=", area_of_triangle(base, height))

    elif choice == 16:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        print("Area of the rectangle with length", length, "and width", width, "=", area_of_rectangle(length, width))

    elif choice == 17:
        side = float(input("Enter the side of the square: "))
        print("Area of the square with side", side, "=", area_of_square(side))
    
    elif choice == 18:
        print("Exiting... ")
        break
    else:
        print("Invalid input")


