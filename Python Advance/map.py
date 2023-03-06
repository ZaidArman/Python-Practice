# Python has builtin function i.e., "map", map is often used with lambda
# Example 1
def add1(x): 
    return x+1
print(map(add1, [1,2,3,4])) # answer will be  " <map object at 0x00000158808CBEE0> "
print(map(lambda x: x+1, [1,2,3,4])) # asnwer will be " <map object at 0x00000158808CAEC0> "

#example 2: 
def add(x, y): 
    return x+y
print(map(add,[1,2,3,4],[100,200,300,400])) # asnwer will be " <map object at 0x00000158808CBFD0> "