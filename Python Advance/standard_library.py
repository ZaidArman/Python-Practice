# Standard Libraries in Python
"""
Python exposes a lot of built-in functionality through its standard library.
The standard library is a huge collection of all sort of utilities, ranging from math utilities to debugging to creating graphical user interfaces.
You can find the full list of standard library modules here: https://docs.python.org/3/library/index.html .

Let's introduce how to use a module of the standard library with small examples.

Some of the important modules are:
"""

# 1) 'math' for math utilities
from math import sqrt 
sqrt(4) # 2.0
# OR
import math
math.sqrt(4) # 2.0



# 2) 're' / rejex for regular expressions
import re
# Search for a pattern in a string
text = "The quick brown fox jumps over the lazy dog"
pattern = "brown"
match = re.search(pattern, text)
if match:
    print("Pattern found at position", match.start())
else:
    print("Pattern not found")
# Replace a pattern in a string
text = "The quick brown fox jumps over the lazy dog"
pattern = "brown"
replace_with = "red"
new_text = re.sub(pattern, replace_with, text)
print("New text:", new_text)




# 3) 'datetime' to work with dates
import datetime
# Get the current date and time
now = datetime.datetime.now()
print("Current date and time:", now)

# Format a date as a string
date = datetime.date(2022, 3, 6)
formatted_date = date.strftime("%Y-%m-%d")
print("Formatted date:", formatted_date)



# 4) 'json' to work with JSON
import json
# Convert a Python dictionary to JSON
data = {"name": "ZaidArman", "age": 23, "Country": "Pakistan"}
json_data = json.dumps(data)
print(json_data)
# Convert a JSON string to a Python dictionary
json_data = '{"name": "ZaidArman", "age": 23, "Country": "Pakistan"}'
data = json.loads(json_data)
print(data)



# 5) 'sqlite3' to use SQLite
import sqlite3
# Create a new database and table
conn = sqlite3.connect("example.db")
c = conn.cursor()
c.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
c.execute("INSERT INTO users VALUES (1, 'John')")
conn.commit()

# Query the database
c.execute("SELECT * FROM users")
rows = c.fetchall()
for row in rows:
    print(row)
conn.close()



# 6) 'os' for Operating System utilities
import os
# Get the current working directory
cwd = os.getcwd()
print("Current working directory:", cwd)

# Create a new directory
new_dir = "example_dir"
os.mkdir(new_dir)
print("New directory created:", new_dir)

# List the files in a directory
files = os.listdir(".")
print("Files in current directory:", files)



# 7) 'random' for random number generation
import random
# Generate a random integer
num = random.randint(1, 10)
print("Random number:", num)
# Shuffle a list
list1 = [1, 2, 3, 4, 5]
random.shuffle(list1)
print("Shuffled list:", list1)



# 8) 'statistics' for statistics utilities
import statistics
# Calculate the mean of a list of numbers
nums = [1, 2, 3, 4, 5]
mean = statistics.mean(nums)
print("Mean:", mean)
# Calculate the median of a list of numbers
nums = [1, 2, 3, 4, 5]
median = statistics.median(nums)
print("Median:", median)


# 9) 'requests' to perform HTTP network requests
import requests
response = requests.get('https://www.google.com')
print(response.status_code)
print(response.headers)
print(response.text)



# 10) 'http' to create HTTP servers
from http.server import BaseHTTPRequestHandler, HTTPServer
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        message = 'Hello, world!'
        self.wfile.write(bytes(message, 'utf8'))

httpd = HTTPServer(('localhost', 8080), MyHandler)
print('Server running on port 8080...')
httpd.serve_forever()



# 11) 'urllib' to manage URLs
from urllib.parse import urlparse
url = 'https://www.google.com/search?q=python'
parsed_url = urlparse(url)
print(parsed_url.scheme)
print(parsed_url.netloc)
print(parsed_url.path)
print(parsed_url.query)