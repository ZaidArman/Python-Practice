# Inheritance in Python:
"""
Inheritance is a fundamental concept in object-oriented programming that allows classes to inherit properties and methods from other classes. 
In Python, we can implement inheritance by creating a new class that inherits the properties and methods of an existing class.
"""

# Types of Inheritance

# Single inheritance: A subclass inherits the properties and methods of a single parent class.
class Parent:
    pass

class child (Parent):
    pass

# Exampple
class Parent:
    def __init__(self, name, BloodGroup):
        self.name = name
        self.BloodGroup = BloodGroup

    def group(self):
        print(f"The Blood Group of Parent is {self.BloodGroup}")

class Child(Parent):
    def __init__(self, name, ChildGroup):
        super().__init__(name, "Arman")
        self.ChildGroup = ChildGroup

    def child_group(self):
        print(f"The Blood Group of the child is {self.ChildGroup}")

my_child = Child("Zaid", "O+ve")
print(my_child.name)  # output: Zaid
print(my_child.BloodGroup)  # output: Arman
my_child.child_group()  # output: The Blood Group of the child is O+ve


# Multiple inheritance: A subclass inherits the properties and methods of multiple parent classes.
class Father:
    pass

class Mother:
    pass

class child(Father, Mother):
    pass

# Example:
class Father:
    def __init__(self, name):
        self.name = name

class Mother(Father):
    def __init__(self, name, sir_name):
        super().__init__(name)
        self.sir_name = sir_name

class child(Mother):
    def __init__(self, name, sir_name, age):
        super().__init__(name, sir_name)
        self.age = age

my_child = child("Zaid", "Ullah", 23)
print(my_child.name)  # output: Zaid
print(my_child.sir_name)  # output: Ullah
print(my_child.age)  # output: 23


# # Multilevel inheritance: a subclass inherits from a parent class, which in turn inherits from another parent class
class GrandFather:
    pass

class Father(GrandFather):
    pass

class child(Father):
    pass

# Example:
class GrandFather:
    def __init__(self, name):
        self.name = name

class Father(GrandFather):
    def __init__(self, name, sir_name):
        super().__init__(name)
        self.sir_name  = sir_name
        
class Child(Father):
    def __init__(self, name, sir_name, generation, age):
        super().__init__(name, sir_name)
        self.generation = generation
        self.age = age

my_child = Child("Zaid", "Ullah", "5G", 23)
print(my_child.name)  # output: Zaid
print(my_child.sir_name)  # output: Ullah
print(my_child.generation) # ourput: 5G
print(my_child.age)  # output: 23



# # Hierarchical Inheritance: 
class Father:
    pass 

class Brother:
    pass

class Sister:
    pass


# Example:
class Father:
    def __init__(self, name):
        self.name = name

    def BloodGroup(self):
        print("The Blood Group of Father is A +ve.")

class Brother(Father):
    def __init__(self, name):
        super().__init__(name)

    def BroGroup(self):
        print("The Brother Group is AB +ve ")

class Sister(Father):
    def __init__(self, name):
        super().__init__(name)

    def SisGroup(self):
        print("The Sis Group is B +ve ")

# Creating objects of the brother and sister classes
my_Brother = Brother("Zaid")
my_Sister = Sister("Arman")

# Accessing attributes and methods of the father, brother and sister classes
print(my_Brother.name)  # Output: Zaid
my_Brother.BroGroup()  # Output: The Brother Group is AB +ve.

print(my_Sister.name)  # Output: Arman
my_Sister.SisGroup()  # Output: The Sis Group is B +ve 

