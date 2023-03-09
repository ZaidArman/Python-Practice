import math

def scientific_calculator():
    print("Welcome to the scientific calculator!")
    while True:
        print("\nPlease choose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Square root")
        print("7. Trigonometric Functions")
        print("8. Logarithmic Functions")
        print("9. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 + num2
            print("Result: ", result)
        
        elif choice == 2:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 - num2
            print("Result: ", result)
        
        elif choice == 3:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 * num2
            print("Result: ", result)
        
        elif choice == 4:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 / num2
            print("Result: ", result)
        
        elif choice == 5:
            num1 = float(input("Enter base: "))
            num2 = float(input("Enter power: "))
            result = math.pow(num1, num2)
            print("Result: ", result)
        
        elif choice == 6:
            num = float(input("Enter number: "))
            result = math.sqrt(num)
            print("Result: ", result)
        
        elif choice == 7:
            print("\nPlease choose a trigonometric function:")
            print("1. Sine")
            print("2. Cosine")
            print("3. Tangent")
            choice2 = int(input("Enter your choice: "))
            num = float(input("Enter angle in radians: "))
            if choice2 == 1:
                result = math.sin(num)
            elif choice2 == 2:
                result = math.cos(num)
            elif choice2 == 3:
                result = math.tan(num)
            else:
                print("Invalid choice")
                continue
            print("Result: ", result)
        
        elif choice == 8:
            print("\nPlease choose a logarithmic function:")
            print("1. Log base 10")
            print("2. Natural logarithm (log base e)")
            choice2 = int(input("Enter your choice: "))
            num = float(input("Enter number: "))
            if choice2 == 1:
                result = math.log10(num)
            elif choice2 == 2:
                result = math.log(num)
            else:
                print("Invalid choice")
                continue
            print("Result: ", result)
        
        elif choice == 9:
            print("Exiting...")
            break
        
        else:
            print("Invalid choice")
            
scientific_calculator()
