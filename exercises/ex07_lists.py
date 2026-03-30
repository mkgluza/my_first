# Exercise 7: Lists
# Task: Create a list of 5 fruits.
# - Print the first and last item.
# - Add a new fruit to the list.
# - Remove one fruit.
# - Print the final list and its length.

# Write your code below:
fruits = ["apple", "banana", "mango", "avocado", "arbuz"]
fruits.append("grape")

first, last = fruits[0], fruits[-1]
print(first, last)
fruits.remove("banana")
print(fruits, len(fruits))
