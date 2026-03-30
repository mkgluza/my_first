# Exercise 9: Dictionaries
# Task: Create a dictionary representing a person with keys:
#   "name", "age", "city"
# - Print each key and value.
# - Update the city to a new value.
# - Add a new key "hobby" with a value of your choice.
# - Print the updated dictionary.

# Write your code below:


journal = {"name": "Michał", "age": 29, "city": "Łodygowice"}

print(journal.keys())
print(journal.values())
journal["city"] = "Bielsko-Biała"
journal["hobby"] = "Learning Python"


print(journal)
