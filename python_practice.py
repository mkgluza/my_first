# ============================================================
# PYTHON PRACTICE — Road to QA Automation Engineer
# Work through this file top to bottom.
# Each section has:
#   [FIX THIS]  — broken code, find and fix the bug
#   [YOUR TURN] — write it yourself
# Run the file often: python python_practice.py
# ============================================================


# ============================================================
# CHAPTER 1: FUNCTIONS
# ============================================================
# A function is a reusable block of code.
# You DEFINE it once, then CALL it many times.
#
# Syntax:
#   def function_name(parameter):
#       return something
#
# Key rules:
#   - starts with "def"
#   - parameters are inputs (optional)
#   - "return" sends a value back (optional)
#   - body must be INDENTED
# ============================================================

print("=" * 40)
print("CHAPTER 1: FUNCTIONS")
print("=" * 40)

# --- 1.1 [FIX THIS] ---
# This function should print "Hello, [name]!"
# There are 3 bugs — find and fix them.


def greet(name):  # bug 1
    print(f"Hello {name}!")  # bug 2 (missing punctuation — the "!" at the end)


greet("Michał")  # bug 3


# --- 1.2 [FIX THIS] ---
# This function should return the sum of two numbers.
# Something is missing inside the function body.


def add_numbers(a, b):
    result = a + b
    return result


print(add_numbers(3, 4))  # should print 7


# --- 1.3 [FIX THIS] ---
# Default parameters — if no greeting is given, use "Hello"
# Fix the bug on the def line.


def greet_with_default(name, greeting="Hello"):  # bug here
    return f"{greeting}, {name}!"


print(greet_with_default("Michal"))  # should print: Hello, Michal!
print(greet_with_default("Michal", "Hi"))  # should print: Hi, Michal!


# --- 1.4 [YOUR TURN] ---
# Write a function called is_even(n) that:
# - returns True if n is even
# - returns False if n is odd
# Hint: use the % operator (remainder). If n % 2 == 0, it's even.
# Then call it and print results for: 4, 7, 0


# Write below:
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


print("is even? ", is_even(4))
print("is even? ", is_even(7))
print("is even? ", is_even(0))
# --- 1.5 [YOUR TURN] ---
# Write a function called multiply_list(numbers) that:
# - takes a LIST of numbers
# - returns all of them multiplied together
# - do NOT use any built-in function
# Example: multiply_list([2, 3, 4]) should return 24  (2 * 3 * 4)
# Hint: start with result = 1, then loop through the list and multiply


# Write below:
def multiply_list(numbers):
    result = 1
    for i in numbers:
        result = i * result
    return result


print(multiply_list([2, 3, 4]))

# ============================================================
# CHAPTER 2: DICTIONARIES
# ============================================================
# A dictionary stores KEY: VALUE pairs.
# Think of it like a real dictionary: word (key) -> definition (value)
#
# Syntax:
#   person = {
#       "name": "Michal",
#       "age": 29
#   }
#
# Access value:   person["name"]     -> "Michal"
# Add new key:    person["city"] = "Krakow"
# All keys:       person.keys()
# All values:     person.values()
# Loop through:   for key, value in person.items()
# ============================================================

print("\n" + "=" * 40)
print("CHAPTER 2: DICTIONARIES")
print("=" * 40)

# --- 2.1 [FIX THIS] ---
# This should create a dictionary and print the name.
# Two bugs — wrong brackets and wrong access syntax.

person = {"name": "Michal", "age": 29}  # bug 1 (wrong brackets)
print(person["name"])  # bug 2 (wrong access syntax)


# --- 2.2 [FIX THIS] ---
# This should print all keys and all values.
# Two bugs in the method names.

car = {"brand": "Audi", "year": 2017}
car["color"] = "black"
print(car.keys())  # bug 1
print(car.values())  # bug 2


# --- 2.3 [FIX THIS] ---
# Loop through a dictionary and print each key and value like:
# "brand: Audi"
# "year: 2017"
# One bug on the for line.

car = {"brand": "Audi", "year": 2017}
for key, value in car.items():  # bug here
    print(f"{key}: {value}")


# --- 2.4 [YOUR TURN] ---
# Create a dictionary called "person" with keys: name, age, city
# a) Print only the keys
# b) Print only the values
# c) Add key "job" with value "tester"
# d) Print the full updated dictionary

# Write below:
person = {"name": "Michał", "age": 29, "city": "Łodygowice"}
print(person.keys())
print(person.values())


# --- 2.5 [YOUR TURN] ---
# Write a function word_count(sentence) that returns a dictionary
# showing how many times each word appears.
# Example:
# word_count("the cat sat on the mat") -> {"the": 2, "cat": 1, "sat": 1, "on": 1, "mat": 1}
# Hints:
#   - sentence.split() splits a string into a list of words
#   - start with an empty dict {}
#   - loop through words: if word already in dict, add 1. If not, set to 1.

# Write below:


def word_count(sentence):
    counts = {}
    for word in sentence.split():
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


print(word_count("the cat sat on the mat"))


# ============================================================
# CHAPTER 3: CLASSES
# ============================================================
# A class is a blueprint for creating objects.
# Example: "Car" is a class. Your specific Audi 2017 is an object.
#
# Syntax:
class Car:
    def __init__(self, brand, year):  # runs when object is created
        self.brand = brand  # store as attribute
        self.year = year

    def describe(self):  # method (function inside class)
        print(f"This is a {self.year} {self.brand}.")


my_car = Car("Audi", 2017)  # create object
my_car.describe()  # call method

# Key rules:
#   - __init__ always has "self" as first parameter
#   - every method has "self" as first parameter
#   - self.attribute stores the value on the object
# ============================================================

print("\n" + "=" * 40)
print("CHAPTER 3: CLASSES")
print("=" * 40)

# --- 3.1 [FIX THIS] ---
# Two bugs — one on the __init__ line, one on the last line.


class Car:
    def __init__(self, brand, year):  # bug 1 (missing something)
        self.brand = brand
        self.year = year

    def describe(self):
        print(f"This is a {self.year} {self.brand}.")


my_car = Car("Audi", 2017)
my_car.describe()  # bug 2 (missing something)
# --- 3.2 [FIX THIS] ---
# This class tracks a bank balance.
# One bug inside the deposit method.


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = +amount  # bug: should ADD to balance, not replace it

    def show_balance(self):
        print(f"{self.owner} has {self.balance} PLN")


account = BankAccount("Michal", 100)
account.deposit(50)
account.show_balance()  # should print: Michal has 150 PLN


# --- 3.3 [YOUR TURN] ---
# Create a class called Dog with:
# - attributes: name, breed
# - method bark() that prints: "Woof! I am [name]."
# - method info() that prints: "[name] is a [breed]."
# Create two Dog objects and call both methods on each.


# Write below:
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        self.bark = "Woof! I am "
        print(f"{self.bark} {self.name}")

    def info(self):
        print(f"{self.name} {self.breed}")


dog_info = Dog("Rambo", "Husky")
dog_info.bark()
dog_info.info()


# ============================================================
# CHAPTER 4: ERROR HANDLING
# ============================================================
# When code crashes, Python raises an Exception.
# You can CATCH it with try/except so the program doesn't crash.
#
# Syntax:
#   try:
#       risky code here
#   except SomeError:
#       what to do if it crashes
#
# Common exceptions:
#   ZeroDivisionError  — dividing by zero
#   FileNotFoundError  — file doesn't exist
#   KeyError           — key not in dictionary
#   ValueError         — wrong type of value (e.g. int("hello"))
#   TypeError          — wrong type (e.g. "hello" + 5)
# ============================================================

print("\n" + "=" * 40)
print("CHAPTER 4: ERROR HANDLING")
print("=" * 40)

# --- 4.1 [FIX THIS] ---
# "except:" catches ALL errors — that's bad practice.
# Fix it to catch only ZeroDivisionError.


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:  # bug: be specific  # noqa: E722
        return "Cannot divide by zero"


print(safe_divide(10, 2))  # should print: 5.0
print(safe_divide(10, 0))  # should print: Cannot divide by zero


# --- 4.2 [FIX THIS] ---
# Same problem — fix the except line to catch only FileNotFoundError.


def read_file(filename):
    try:
        file = open(filename, "r")
        return file.read()
    except FileNotFoundError:  # bug: be specific
        return f"Error: file '{filename}' not found"


print(read_file("nonexistent.txt"))


# --- 4.3 [YOUR TURN] ---
# Write a function called safe_divide(a, b) that:
# - Returns a / b if b is not 0
# - Returns "Cannot divide by zero" if b is 0
# - Use try/except ZeroDivisionError
# Test it with: safe_divide(10, 2) and safe_divide(5, 0)


# Write below:
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"


print(safe_divide(10, 2))
print(safe_divide(5, 0))

# --- 4.4 [YOUR TURN] ---
# Write a function get_value(dictionary, key) that:
# - Returns the value for the given key
# - If the key doesn't exist, returns "Key not found"
# - Use try/except KeyError
# Test it with: {"name": "Michal"}, key="name" and key="age"


# Write below:
def get_value(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        return "Key not found"


print(get_value({"name": "Michał"}, "name"))
print(get_value({"name": "Michał"}, "age"))

# ============================================================
# CHAPTER 5: MINI PROJECT — Student Gradebook
# ============================================================

print("\n" + "=" * 40)
print("CHAPTER 5: MINI PROJECT")
print("=" * 40)

# --- 5.1 [YOUR TURN] ---
# Create a class called Student with:
# - attributes: name, grades (empty list by default)
# - method add_grade(grade) — appends a grade to the list
# - method average() — returns the average grade (return 0 if no grades yet)
# - method report() — prints:
#   "Student: [name] | Grades: [grades] | Average: [average]"
#
# Create 2 students, add some grades, print their reports.


# Write below:
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def report(self):
        avg = self.average()
        print(f"Student: {self.name} | Grades: {self.grades} | Average: {avg}")


michal = Student("Michał")
mateusz = Student("Mateusz")

michal.add_grade(5)
michal.add_grade(4)

mateusz.add_grade(3)
mateusz.add_grade(6)

michal.report()
mateusz.report()


# ============================================================
# DONE WITH A CHAPTER? Run: python python_practice.py
# Then paste the file here for review.
# ============================================================
