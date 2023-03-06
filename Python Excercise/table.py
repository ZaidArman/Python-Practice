"""
Excercise:
Write a program which does the following:
- Take a number input from the console sample input
- We need to output to the console the multiplication table for that number using the "for" loop in the format given in the IDE
"""

a = int(input(" Enter a number for table: "))
for i in range(1,11):
  print(" Table of ", a, 'x', i, '=', a * i)