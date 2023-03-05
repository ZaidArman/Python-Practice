# Continue Statement
"""
With the "continue" statement we achieve the following
We can stop the current iteration of the loop
We continue with the next element. That is, we will not go any further in this particular iteration, 
and instead skip to the next iteration.
"""
months = ["Jan", "Feb", "March","Apr","May"]
for x in months:
  if x == "Apr":
     continue
  print(x)

#Break Statement
"""
We can use the "break" statement to stop the loop before it has looped through all the items.

Note:
"break" functions differently from "continue".
"break" exits the loop completely and goes to the next section of the program
"continue" exits the current iteration and skips the code remaining in the current loop iteration.
However, the "for" or "while" loop continues with the next iteration.
"""

for i in range(11): 
    if i == 8:
        break
    #Note that print is being executed AFTER the if / break condition.
    #We need to go till i = 8 since we want to print till 7
    print(i)