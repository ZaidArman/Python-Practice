# NumPy:
"""
NumPy is a Python library for working with arrays and matrices. 
It provides a powerful N-dimensional array object, as well as functions for working with these arrays. 
NumPy is widely used in scientific computing, data analysis, and machine learning, 
as it provides fast and efficient numerical operations on large arrays and matrices.
NumPy arrays are similar to Python lists, but they are homogeneous (i.e., all elements have the same type) and can be multi-dimensional. 
This makes them ideal for mathematical operations, as they can be used to represent vectors, matrices, and tensors.
NumPy also provides a wide range of functions for manipulating arrays, including 
mathematical functions (e.g., sin, cos, exp), 
statistical functions (e.g., mean, median, standard deviation), and 
linear algebra functions (e.g., matrix multiplication, eigenvalues and eigenvectors). 
It also provides tools for working with data in various formats, including CSV, HDF5, and NumPy's own binary format (NPY and NPZ).
"""

import numpy as np # Import NumPy as np, or we can import as any word

# we can create a NumPy array from a list using np.array().
numbers = [1, 2, 3, 4, 5] # Create a list
numbers_array = np.array(numbers) # Convert the list to an array
print(type(numbers_array)) # Print the type of numbers_array

# We can perform mathematical operations on a NumPy array as you would with a value.
numbers_multiplied = numbers * 10 # Multiply the array by 10
print(numbers_multiplied) # Print the array

# We can subset an array in the same way you would with a list, using square brackets `[]` and colons ':'.
sales = np.array([110, 260, 50, 390, 30]) # Create an another array
first_sales = sales[0:2] # Subset the array
print(first_sales) # Print the subset

# can also use operators such as `<` and `>` to create a Boolean NumPy array. You can then use the Boolean array to subset your original array
large_sales = sales > 100 # Create a Boolean array
print(sales[large_sales]) # Subset the original array

# We can use functions such as np.mean(), np.median(), and np.std() to generate summary statistics of NumPy arrays.
print("mean of a sales: ", np.mean(sales)) # Calculate the average
print("median of a sales: ", np.median(sales)) # Calculate the median
print("Standard deraivtion of a sales: ", np.std(sales)) # Calculate the standard deviation

# We You can also use `np.corrcoef()` to calculate the correlation between two NumPy arrays.
SALES = np.array([190, 210, 185, 235, 170, 270, 240, 225]) # Create a NumPy array of SALES
MARKETING = np.array([35, 50, 45, 110, 85, 95, 70, 80]) # Create a NumPy array of marketing expenses
print("# correlation b/t SALES and Marketing: ", np.corrcoef(SALES, MARKETING)) # Calculate the correlation between the two arrays
