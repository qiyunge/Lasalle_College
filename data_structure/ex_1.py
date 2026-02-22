"""
Python Basics - Student Learning Materials
"""

# ============================================================================
# 1. BASIC OUTPUT
# ============================================================================
print("Hello, World!")

# ============================================================================
# 2. VARIABLES AND CONDITIONALS
# ============================================================================
x = 1
if x == 1:
    print("x is 1.")

# ============================================================================
# 3. STRINGS
# ============================================================================
a = "I am a teacher"
print(a.split())

one, two, three = "Hello", "World", 7
print(one + " " + two + " " + str(three))

# ============================================================================
# 4. DATA TYPES AND TYPE CONVERSION
# ============================================================================
c = float(7)
print(c)

b = 3.14
print(b.is_integer())

# ============================================================================
# 5. FUNCTIONS
# ============================================================================
def is_integer(n):
    """Check if a number is an integer mathematically (no decimal part)."""
    return n % 1 == 0

print(f"Is {b} an integer? {is_integer(b)}")
print(f"Is {c} an integer? {is_integer(c)}")

# ============================================================================
# 6. LISTS - CREATION AND BASICS
# ============================================================================
my_list = [1, 2, 3, 4, 5]
my_list_2 = ["Hello", 1, 3.14]  # Mixed types

# ============================================================================
# 7. LISTS - ADDING ELEMENTS
# ============================================================================
my_list.append(10)           # Adds one element
my_list.extend([20, 30])     # Adds multiple elements
print(my_list)

# ============================================================================
# 8. ITERABLES
# ============================================================================
my_tuple = (4, 5, 6)
my_string = "abc"
my_range = range(3)

my_list.extend(my_tuple)     # Extend with tuple
my_list.extend(my_string)    # Extend with string (adds chars)
print("After extending:", my_list)

# ============================================================================
# 9. LIST INDEXING
# ============================================================================
dog_names = ["Max", "Bella", "Charlie", "Lucy", "Cooper", "Luna", "Buddy", "Daisy", "Rocky", "Molly"]
print(f"First: {dog_names[0]}, Last: {dog_names[-1]}")

# ============================================================================
# 10. LOOPS
# ============================================================================
for index, name in enumerate(dog_names):
    print(f"Index {index}: {name}")

# Filtering with loops
names_with_c = []
for name in dog_names:
    if name[0] == "C":
        names_with_c.append(name)
print(names_with_c)

# ============================================================================
# 11. LIST COMPREHENSIONS
# ============================================================================
names_with_c_2 = [name for name in dog_names if name[0] == "C"]
print(names_with_c_2)

# ============================================================================
# 12. DICTIONARIES
# ============================================================================
# Creating dictionaries
student_grades = {"Alice": 95, "Bob": 87, "Charlie": 92}
print(f"Alice's grade: {student_grades['Alice']}")

# Adding/updating entries
student_grades["Diana"] = 88
student_grades["Bob"] = 90  # Update existing
print(student_grades)

# Iterating over dictionaries
for name, grade in student_grades.items():
    print(f"{name}: {grade}")

# Dictionary methods
print(f"Keys: {list(student_grades.keys())}")
print(f"Values: {list(student_grades.values())}")

# ============================================================================
# 13. SETS
# ============================================================================
# Creating sets
unique_numbers = {1, 2, 3, 4, 5}
print(unique_numbers)

# Sets automatically remove duplicates
numbers_with_duplicates = {1, 2, 2, 3, 3, 4}
print(numbers_with_duplicates)  # Only unique values

# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(f"Union: {set_a | set_b}")
print(f"Intersection: {set_a & set_b}")
print(f"Difference: {set_a - set_b}")

# ============================================================================
# 14. IMPORTS
# ============================================================================
import random
print(f"Random number: {random.randint(1, 10)}")