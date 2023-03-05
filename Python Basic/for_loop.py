# For loop
a = "SyntheticProgrammer"
for x in a:
 print(x)
 
 
 # use the range key-words in for loop
 for x in range( 10 ): # range = 10
     print(x)
print("Loop Ended! ")

# The range() function can also return a custom sequence of numbers by defining the starting and ending values separated by a comma. 
# i.e., in this range - range(3,15) the loop will start with 3 and end with 14.
for x in range( 3 , 14 ):
  print(x)
  
# it is also possible to specify the increment value by adding a third parameter.
i = 20
for i in range(20, 45, 2 ): # incremented by 2
  print( i )
  
