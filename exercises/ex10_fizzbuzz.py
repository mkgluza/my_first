# Exercise 10: FizzBuzz
# Task: Loop through numbers 1 to 50.
# - Print "Fizz" if the number is divisible by 3.
# - Print "Buzz" if the number is divisible by 5.
# - Print "FizzBuzz" if divisible by both 3 and 5.
# - Otherwise, print the number.

# Write your code below:


for number in range(1, 51):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")

    elif number % 3 == 0:
        print("Fizz")

    elif number % 5 == 0:
        print("Buzz")

    else:
        print(number)
