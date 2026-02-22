"""
Practice Examples - Based on python_1.py, python_2.py, python_3.py, and python_4.py
Complete the following exercises to practice Python concepts
"""

# ============================================================================
# EXERCISE 1: Variables and Conditionals
# ============================================================================
# TODO: Create a variable called 'temperature' and set it to 25
# TODO: Write an if-else statement that prints "It's hot!" if temperature > 20, 
#       otherwise prints "It's cool!"

# Your code here:
temperature = 25
if temperature > 20:
    print("It's hot!")
else:
    print("It's cool!")


# ============================================================================
# EXERCISE 2: String Operations
# ============================================================================
# TODO: Create a string variable with your name
# TODO: Use string concatenation to create "Hello, [Your Name]!"
# TODO: Print the length of your name
# TODO: Print your name in uppercase

# Your code here:
name = "Ali"
greeting = "Hello, " + name + "!"
print(greeting)
print(f"Length of name: {len(name)}")
print(f"Uppercase: {name.upper()}")


# ============================================================================
# EXERCISE 3: Lists - Basic Operations
# ============================================================================
# TODO: Create a list of your favorite fruits (at least 5)
# TODO: Add a new fruit using append()
# TODO: Add multiple fruits using extend()
# TODO: Print the first and last fruit in the list

# Your code here:
fruits = ["apple", "banana", "orange", "grape", "mango"]
fruits.append("strawberry")
fruits.extend(["kiwi", "pineapple"])
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")


# ============================================================================
# EXERCISE 4: List Comprehensions
# ============================================================================
# TODO: Create a list of numbers from 1 to 10
# TODO: Use list comprehension to create a new list with only even numbers
# TODO: Use list comprehension to create a list of squares (n^2) for numbers 1-5

# Your code here:
numbers = list(range(1, 11))
even_numbers = [n for n in numbers if n % 2 == 0]
squares = [n**2 for n in range(1, 6)]
print(f"Even numbers: {even_numbers}")
print(f"Squares: {squares}")


# ============================================================================
# EXERCISE 5: Loops
# ============================================================================
# TODO: Use a for loop to print numbers from 1 to 5
# TODO: Use a while loop to count down from 5 to 1
# TODO: Use enumerate() to print index and value for items in your fruits list

# Your code here:
print("\nFor loop 1-5:")
for i in range(1, 6):
    print(i)

print("\nWhile loop countdown:")
count = 5
while count > 0:
    print(count)
    count -= 1

print("\nEnumerate fruits:")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")


# ============================================================================
# EXERCISE 6: Dictionaries
# ============================================================================
# TODO: Create a dictionary called 'student' with keys: name, age, grade
# TODO: Add a new key 'city' to the dictionary
# TODO: Update the 'grade' value
# TODO: Loop through and print all key-value pairs

# Your code here:
student = {
    "name": "Alice",
    "age": 20,
    "grade": 85
}
student["city"] = "Montreal"
student["grade"] = 90
print("\nStudent dictionary:")
for key, value in student.items():
    print(f"{key}: {value}")


# ============================================================================
# EXERCISE 7: Sets
# ============================================================================
# TODO: Create two sets: set1 = {1, 2, 3, 4, 5} and set2 = {4, 5, 6, 7, 8}
# TODO: Find and print the intersection
# TODO: Find and print the union
# TODO: Find and print the difference (set1 - set2)

# Your code here:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(f"\nSet1: {set1}")
print(f"Set2: {set2}")
print(f"Intersection: {set1.intersection(set2)}")
print(f"Union: {set1.union(set2)}")
print(f"Difference (set1 - set2): {set1.difference(set2)}")


# ============================================================================
# EXERCISE 8: Functions
# ============================================================================
# TODO: Write a function called 'multiply' that takes two parameters and returns their product
# TODO: Write a function called 'greet' that takes a name parameter and prints "Hello, [name]!"
# TODO: Call both functions with sample values

# Your code here:
def multiply(a, b):
    return a * b

def greet(name):
    print(f"Hello, {name}!")

print(f"\nMultiply 5 * 3 = {multiply(5, 3)}")
greet("Python")


# ============================================================================
# EXERCISE 9: Lambda Functions
# ============================================================================
# TODO: Create a lambda function to add two numbers
# TODO: Create a lambda function to check if a number is even
# TODO: Use the lambda functions with sample values

# Your code here:
add = lambda x, y: x + y
is_even = lambda n: n % 2 == 0

print(f"\nLambda add(10, 5) = {add(10, 5)}")
print(f"Is 8 even? {is_even(8)}")
print(f"Is 7 even? {is_even(7)}")


# ============================================================================
# EXERCISE 10: Generators
# ============================================================================
# TODO: Create a generator function called 'countdown' that yields numbers from n down to 1
# TODO: Use the generator in a for loop to print the countdown from 5

# Your code here:
def countdown(n):
    while n > 0:
        yield n
        n -= 1

print("\nCountdown generator:")
for num in countdown(5):
    print(f"T-minus {num}...")


# ============================================================================
# EXERCISE 11: String Methods
# ============================================================================
# TODO: Create a string "Python Programming"
# TODO: Check if it starts with "Python"
# TODO: Check if it ends with "ing"
# TODO: Split it into words
# TODO: Count how many times 'm' appears

# Your code here:
text = "Python Programming"
print(f"\nText: {text}")
print(f"Starts with 'Python': {text.startswith('Python')}")
print(f"Ends with 'ing': {text.endswith('ing')}")
print(f"Words: {text.split()}")
print(f"Count of 'm': {text.count('m')}")


# ============================================================================
# EXERCISE 12: Classes and Objects
# ============================================================================
# TODO: Create a class called 'Book' with __init__ method
# TODO: Include attributes: title, author, pages
# TODO: Add a method called 'info' that returns a string with book information
# TODO: Create an instance of Book and call the info method

# Your code here:
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def info(self):
        return f"{self.title} by {self.author}, {self.pages} pages"

my_book = Book("Python Basics", "John Doe", 300)
print(f"\nBook info: {my_book.info()}")


# ============================================================================
# EXERCISE 13: Boolean Operators
# ============================================================================
# TODO: Create variables: age = 25, has_license = True
# TODO: Write a condition that checks if age >= 18 AND has_license is True
# TODO: Print "Can drive" if condition is True, otherwise "Cannot drive"

# Your code here:
age = 25
has_license = True
if age >= 18 and has_license:
    print("\nCan drive")
else:
    print("\nCannot drive")


# ============================================================================
# EXERCISE 14: List Filtering
# ============================================================================
# TODO: Create a list of numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# TODO: Use a loop to create a new list with only numbers greater than 5
# TODO: Do the same using list comprehension

# Your code here:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
greater_than_5_loop = []
for num in numbers:
    if num > 5:
        greater_than_5_loop.append(num)

greater_than_5_comprehension = [num for num in numbers if num > 5]
print(f"\nNumbers > 5 (loop): {greater_than_5_loop}")
print(f"Numbers > 5 (comprehension): {greater_than_5_comprehension}")


# ============================================================================
# EXERCISE 15: String Slicing
# ============================================================================
# TODO: Create a string "Hello World"
# TODO: Print the first 5 characters
# TODO: Print characters from index 6 to the end
# TODO: Print the string reversed

# Your code here:
message = "Hello World"
print(f"\nFirst 5 chars: {message[:5]}")
print(f"From index 6: {message[6:]}")
print(f"Reversed: {message[::-1]}")


# ============================================================================
# EXERCISE 16: Break and Continue
# ============================================================================
# TODO: Use a for loop to print numbers 1-10, but skip 5 using continue
# TODO: Use a while loop with break to print numbers 1-5

# Your code here:
print("\nNumbers 1-10 (skipping 5):")
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

print("\nNumbers 1-5 (using break):")
num = 1
while True:
    print(num)
    num += 1
    if num > 5:
        break


# ============================================================================
# EXERCISE 17: Type Checking
# ============================================================================
# TODO: Create variables of different types: int, float, str, list
# TODO: Use isinstance() to check each variable's type
# TODO: Print the type of each variable

# Your code here:
my_int = 42
my_float = 3.14
my_str = "Hello"
my_list = [1, 2, 3]

print(f"\nType checks:")
print(f"my_int is int: {isinstance(my_int, int)}")
print(f"my_float is float: {isinstance(my_float, float)}")
print(f"my_str is str: {isinstance(my_str, str)}")
print(f"my_list is list: {isinstance(my_list, list)}")


# ============================================================================
# EXERCISE 18: Dictionary Operations
# ============================================================================
# TODO: Create a phonebook dictionary with at least 3 contacts
# TODO: Add a new contact
# TODO: Remove a contact using del
# TODO: Remove a contact using pop() and print the popped value
# TODO: Print all keys and all values separately

# Your code here:
phonebook = {
    "Alice": "555-0101",
    "Bob": "555-0102",
    "Charlie": "555-0103"
}
phonebook["Diana"] = "555-0104"
del phonebook["Alice"]
popped_phone = phonebook.pop("Bob")
print(f"\nPopped phone number: {popped_phone}")
print(f"Keys: {list(phonebook.keys())}")
print(f"Values: {list(phonebook.values())}")
print(f"Remaining phonebook: {phonebook}")