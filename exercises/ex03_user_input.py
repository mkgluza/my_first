# Exercise 3: User Input
# Task: Ask the user for their name and age.
# Then print: "Hello, <name>! You are <age> years old."

# Write your code below:

name = input("What's your name: ")
age = int(input("What's your age: "))

# A little extra for my own entertainment.

if age >= 18:
    print(f"\n{name}, you are {age} years old.\nCongratulations, you can buy a beer !!")

else:
    print(f"\n{name}, you are {age} years old.\nNo beer for you kiddo")
