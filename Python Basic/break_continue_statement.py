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
  
  