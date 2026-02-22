# Generators
# A generator is a function that returns a sequence of values
# It uses the yield keyword to return a value and pause the function
# It can be used to create a sequence of values
import random

def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1, 15)

for random_number in lottery():
       print("And the next number is... %d!" %(random_number))

lot = lottery()
print(lot)
print(next(lot))

# list comprehension without list comprehension
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
      if word != "the":
          word_lengths.append(len(word))
print(words)
print(word_lengths)

# list comprehension
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]
print(words)
print(word_lengths)


# Set
print(set("my name is Eric and Eric is my name".split()))


a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.intersection(b))
print(b.intersection(a))

a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.difference(b))
print(b.difference(a))

a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.union(b))


# lambda function
def sum(a,b):
    return a + b

a = 1
b = 2
c = sum(a,b)
print(c)

# your_function_name = lambda inputs : expression

a = 1
b = 2
sum = lambda x,y : x + y
c = sum(a,b)
print(c)
