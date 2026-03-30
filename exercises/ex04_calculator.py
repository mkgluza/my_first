# Exercise 4: Simple Calculator
# Task: Ask the user for two numbers.
# Print the result of: addition, subtraction, multiplication, and division.

# Write your code below:


num1 = int(input("your first number here: "))
num2 = int(input("your second number here: "))


print(f"addition: {num1 + num2}")
print(f"subtraction: {num1 - num2}")
print(f"multiplication: {num1 * num2}")


# A little warning for the user
if num2 == 0:
    print("Cannot divide by zero!")
else:
    print(f"division: {num1 / num2}")
