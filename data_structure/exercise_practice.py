"""
Practice Exercises - Based on ex_1.py, ex_2.py, ex_3.py

Instructions:
- Complete each TODO.
- Run this file to check your outputs.
- Do not import extra libraries unless a task asks you to.
"""

# ============================================================================
# 1. BASIC OUTPUT
# ============================================================================
# TODO: Print "Hello, Python Practice!"


# ============================================================================
# 2. VARIABLES AND CONDITIONALS
# ============================================================================
# TODO: Create a variable `x` with value 7. If x is odd, print "odd", else "even".


# ============================================================================
# 3. STRINGS
# ============================================================================
# TODO: Given the string below, print it reversed.
message = "Practice makes progress"


# TODO: Split the string below by spaces and print the list.
quote = "Learn by doing"


# ============================================================================
# 4. TYPE CONVERSION
# ============================================================================
# TODO: Convert "3.5" to a float and print whether it is an integer.


# ============================================================================
# 5. FUNCTIONS
# ============================================================================
def is_integer(n):
    """Return True if n is a whole number, else False."""
    # TODO: Implement using modulus or int comparison.
    pass


def multiply_list(numbers, factor):
    """Return a new list where each number is multiplied by factor."""
    # TODO: Implement using a list comprehension.
    pass


# ============================================================================
# 6. LISTS
# ============================================================================
nums = [1, 2, 3, 4, 5]
# TODO: Append 6, then extend with [7, 8]. Print the final list.


# TODO: Create a list of squares from nums and print it.


# ============================================================================
# 7. LIST FILTERING
# ============================================================================
dog_names = ["Max", "Bella", "Charlie", "Lucy", "Cooper", "Luna", "Buddy", "Daisy", "Rocky", "Molly"]
# TODO: Build a list of names that start with "C" using a loop.


# TODO: Do the same with a list comprehension and print both lists.


# ============================================================================
# 8. DICTIONARIES
# ============================================================================
student_grades = {"Alice": 95, "Bob": 87, "Charlie": 92}
# TODO: Add "Diana": 88, update "Bob" to 90, then print the dictionary.


# TODO: Print all student names and grades in "Name: Grade" format.


# ============================================================================
# 9. SETS
# ============================================================================
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
# TODO: Print union, intersection, and difference (a - b).


# ============================================================================
# 10. STRING FUNCTIONS
# ============================================================================
def is_palindrome(word):
    """Return True if word is a palindrome (ignore spaces and case)."""
    # TODO: Implement using slicing.
    pass


def is_anagram(word1, word2):
    """Return True if word1 and word2 are anagrams (ignore spaces and case)."""
    # TODO: Implement using sorted().
    pass


# ============================================================================
# 11. LOOPS
# ============================================================================
# TODO: Print numbers 1 to 10, but skip multiples of 3.


# TODO: Use a while loop to print 5, 4, 3, 2, 1.


# ============================================================================
# 12. CLASSES
# ============================================================================
class Person:
    def __init__(self, name, age, city, email):
        self.name = name
        self.age = age
        self.city = city
        self.email = email

    def say_hello(self):
        # TODO: Print "Hello <name>"
        pass

    def authorization(self):
        # TODO: Return authorized message only if age >= 18 and city is "Montreal".
        pass


# ============================================================================
# 13. DICTIONARY PRACTICE
# ============================================================================
phonebook = {}
# TODO: Add three names and numbers, then print the dictionary.


# TODO: Remove one entry using del or pop, then print the result.


# ============================================================================
# 14. MAIN CHECKS
# ============================================================================
if __name__ == "__main__":
    # Quick checks - you can edit expected output once you implement TODOs.
    print("Running quick checks...")
    print(is_integer(3.0))  # True
    print(is_integer(3.5))  # False
    print(multiply_list([1, 2, 3], 3))  # [3, 6, 9]
    print(is_palindrome("racecar"))  # True
    print(is_palindrome("hello"))  # False
    print(is_anagram("listen", "silent"))  # True
    print(is_anagram("hello", "world"))  # False

