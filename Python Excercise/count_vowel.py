# Define a function to count vowels in a string
def count_vowels(string):
    vowels = "aeiou"
    count = 0
    for char in string.lower():
        if char in vowels:
            count += 1
    return count

# Get input from user
string = input("Enter a string: ")
# Count number of vowels in the input string
num_vowels = count_vowels(string)
# Print the result
print(f"The number of vowels in the string is: {num_vowels}")
