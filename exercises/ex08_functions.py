# Exercise 8: Functions
# Task 1: Write a function that takes a name and prints "Hello, <name>!"
# Task 2: Write a function that takes two numbers and returns their sum.
# Call both functions and print the results.

# Write your code below:
def welcoming(name, greeting):
    print(f"{greeting}, {name}!")


welcoming("Michał", "Hello")


def calculation(num1, num2):

    result = num1 + num2

    print(f"{result}")
    return result


calculation(2, 5)
