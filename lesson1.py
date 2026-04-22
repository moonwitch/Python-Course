# Tuple is static list
tuple = (1, "seven", 12)
print(2 in tuple)  # is 2 in the tuple
print(tuple[1])  # print the second element of the tuple

# Lists
numbers = [1, 2, 3, 4, 5, 3]
print(numbers)
numbers.append(6)
print(numbers)
numbers.remove(3)
print(numbers)
numbers.pop(2)
print(numbers)

# Sets
# Sets are unordered collections of unique elements
numbers_set = {1, 2, 3, 4, 5}
print(numbers_set)
numbers_set.add(6)
print(numbers_set)
numbers_set.remove(3)
print(numbers_set)
numbers_set.pop()
print(numbers_set)

# Dictionaries
# Dictionaries are key-value pairs
person = {"name": "John", "age": 30}
print(person)
print(person["name"])
person["age"] = 31
print(person)
person.pop("age")
print(person)

# If - elif - else
# Conditional statements
if person["name"] == "John":
    print("Hello, John!")
elif person["name"] == "Jeb":
    print("Hello, Jeb!")
else:
    print("Hello stranger!")

# Loops
# For loop
for number in numbers:
    print(number)
# While loop
sample = 0
while sample < len(numbers):
    print(numbers[sample])
    sample += 1
