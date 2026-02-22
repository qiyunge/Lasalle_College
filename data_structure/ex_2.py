

# Using Operators with Strings

from tokenize import _all_string_prefixes


helloworld = "hello" + " " + "world"
print(helloworld)

lotsofhellos = "hello" * 10
print(lotsofhellos)

# Using Operators with Lists
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

even_numbers.extend(odd_numbers)
print(even_numbers)

print([1,2,3] * 3)
print("====" * 10)

multiply_list = [x * 3 for x in odd_numbers]
print(multiply_list)

a_string = "Hello, World!"
print(a_string.index("o"))

print(a_string.count("l"))

astring = "Hello world!"
print(astring[3:7])
print(astring[3:])
print(astring[3:7:3])

# Reverse a string
astring = "Hello world!"
print(astring[::-1])

# Check if a word is a palindrome (reads the same forwards and backwards)
def is_palindrome(word):
    word = word.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    return word == word[::-1]

# Examples
# print(is_palindrome("racecar"))  # True
# print(is_palindrome("level"))    # True
# print(is_palindrome("hello"))    # False
# print(is_palindrome("madam"))    # True

# Check if two words are anagrams (contain the same letters)
def is_anagram(word1, word2):
    word1 = word1.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    word2 = word2.lower().replace(" ", "")
    return sorted(word1) == sorted(word2)  # Sort letters and compare

# Examples
print(is_anagram("listen", "silent"))  # True
print(is_anagram("evil", "vile"))      # True
print(is_anagram("hello", "world"))    # False
print(is_anagram("rail safety", "fairy tales"))  # True


astring = "Hello world!"
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

astring = "Hello world!"
afewwords = astring.split(" ")
print(afewwords)

for w in afewwords:
    print(w)