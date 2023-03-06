# Class in Python
"""
A class is a blueprint for creating objects that have common attributes and methods. 
An object is an instance of a class, and it contains all the attributes and methods defined by the class.
"""

# Example 1:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person1 = Person("Zaid", 23)
person2 = Person("Arman", 24)
person1.say_hello()  # Output: Hello, my name is Zaid and I am 23 years old.
person2.say_hello()  # Output: Hello, my name is Arman and I am 24 years old.

# Explanation:
"""
In this example, we have defined a Person class with two attributes (name and age) and one method (say_hello). 
We have created two objects (person1 and person2) of the Person class and called the say_hello method on each object.
"""

# Example 2:
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} successful. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. New balance is {self.balance}.")
        else:
            print("Insufficient funds.")

account1 = BankAccount("123456")
account2 = BankAccount("789012", 500)
account1.deposit(1000)   # Output: Deposit of 1000 successful. New balance is 1000.
account2.withdraw(200)   # Output: Withdrawal of 200 successful. New balance is 300.
account2.withdraw(400)   # Output: Insufficient funds.

# Explanation:
"""
In this example, we have defined a BankAccount class with two attributes (account_number and balance) 
and two methods (deposit and withdraw). 
We have created two objects (account1 and account2) of the BankAccount class and called the deposit 
and withdraw methods on each object to deposit and withdraw money from the accounts.
"""

# Exampl 3:
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)
# Get user input for rectangle dimensions
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))

# Create rectangle object using user input
rectangle = Rectangle(length, width)
# Calculate area and perimeter of rectangle object and print results
area = rectangle.calculate_area()
perimeter = rectangle.calculate_perimeter()

print(f"The area of the rectangle is {area:.2f} square units.")
print(f"The perimeter of the rectangle is {perimeter:.2f} units.")

# Explanation:
"""
In this example, we have defined a Rectangle class with two attributes (length and width) 
and two methods (calculate_area and calculate_perimeter). 
We use input() function to get user input for the length and width of the rectangle. 
We then create a rectangle object using the user input and call the calculate_area 
and calculate_perimeter methods on the object to calculate the area and perimeter of the rectangle.
"""