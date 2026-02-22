# Conditions

from ast import Dict, main


x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True

# Boolean operators
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")


# The 'in' operator
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")


statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True: # else if
    # do something else
    pass
else:
    # do another thing
    pass


# differnce between continue and pass
for x in range(10):
    if x == 5:
        continue
    print(x)

# example for pass
for x in range(10, 20):
    if x == 15:
        pass
    print(x)

# is operator
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False

# why x is y is False?
# because x and y are different objects
# they have the same value, but they are not the same object

# check type with is operator
if isinstance(x, list):
    print("x is a list")


# The "not" operator
print(not False) # Prints out True
print((not False) == (False)) # Prints out False


# The "for" loop
list_primes = [2, 3, 5, 7]
for prime in list_primes:
    print(prime)

# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# Prints out 3,4,5
for x in range(3, 6):
    print(x)

# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)

# The "while" loop
# Prints out 0,1,2,3,4
count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1

# "break" and "continue" statements
# Prints out 0,1,2,3,4

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)

# Can we use "else" clause for loops?
# Prints out 0,1,2,3,4 and then it prints "count value reached 5"
count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")

# function
def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
    print(f" Hello, my name is {username} and I want to say {greeting}")


def sum_two_numbers(a, b):
    return a + b




if __name__ == "__main__":
    my_function_with_args("John", "Hello!")
    result = sum_two_numbers(1, 2)
    print(result)


# classes and objects

class MyClass:
    variable = "blah"

    def say_hello(self, name):
        print(f"Hello {name}")

my_object = MyClass()

my_object.say_hello("John")
print(my_object.variable)


# init
class NumberHolder:

   def __init__(self, number):
       self.number = number

   def returnNumber(self):
       return self.number

var = NumberHolder(number=7)
print(var.returnNumber()) #Prints '7'


class Person:
    def __init__(self, name, age, city, email):
        self.name = name
        self.age = age
        self.city = city
        self.email = email

    def say_hello(self):
        print(f"Hello {self.name}")

    def authorization(self):
        if self.age >= 18 and self.city == "Montreal":
            return "You are authorized to access this resource"
        else:
            return "You are not authorized to access this resource"

person = Person(name="John", age=30, city="Montreal", email="john@example.com")
print(person.authorization())


# dictionary
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)

# iterate over dictionary
for name, phone in phonebook.items():
    print(f"Name: {name}, Phone: {phone}")

# Removing a value
del phonebook["John"]
print(phonebook)

popped_value = phonebook.pop("Jill")
