# Nested Function
"""
Functions in Python can be nested inside other functions.
A function defined inside a function is visible only inside that function.
"""

#Example 1:
def outer():
    def inner(x):
        return x**2
    return inner
square = outer()
result = square(5)
print(result) # Output: 25



# Example 2:
def talk(phrase):
    def say(word_list):
        if not word_list: # Base case: If the list is empty, return from the function
            return
        word = word_list.pop(0) # Get the first word in the list and remove it
        print(word)
        say(word_list) # Recursively call say() with the remaining words in the list

    words = phrase.split(' ')
    say(words) # Call say() with the list of words in the phrase

talk('I am going to buy the milk')


