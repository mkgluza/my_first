# Exercise 5: If / Else
# Task: Ask the user to enter a number.
# Print "Positive" if it's greater than 0,
# "Negative" if it's less than 0,
# or "Zero" if it equals 0.

# Write your code below:
user = input("What's your number: ")
user = int(user)
if user > 0:
    print("Positive")

elif user < 0:
    print("Negative")

elif user == 0:
    print("Zero")
