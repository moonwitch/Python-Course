# Operators
ran = 2
dom = 40
rt = 13
print("1. Print the sum of 2 integers")
print(ran + dom)  # 42
print("2. Print an integer raised to the 2nd power")
print(rt**2)  # 169
print("3. Print `I am with your age behind it")
print(f"I am {ran + dom}")  # I am 42

# Sequences Lists and Sets
list1 = [3, 2, 1, 4]
list2 = [4, 7, 3, 2]

print("1. Concatenate two lists")
list3 = list1 + list2
print(list3)

for x in list2:
    list1.append(x)
print(list1)

# reset
list1 = [3, 2, 1, 4]
list1.extend(list2)
print(list1)

print("2. Sorting")
list1.sort()
print(list1)

print("3. 2d listing")
tdlist = [
    [2.0, 3.1, 4.3],
    [64.4, 0, 2.3],
]
print(tdlist)
tdlist[1][1] = 3
print(tdlist)

# Mapping types
# Dict
dict = {"name": "Jef", "age": 30, "work": False}
print(dict["name"])
dict["work"] = True
dict["hobbies"] = ("reading", "swimming", "walking")

# Statements
# Part 1
var1 = "woop"
var2 = "woopp"
if var1 != var2:
    print("Not equal!")
else:
    print("They're equal!!")
var3 = 5
var4 = 8

if var3 <= var4:
    print(var4)
else:
    print(var3)

# Part 2
input1 = int(input("Enter a number: "))
input2 = int(input("Enter another number: "))
if input1 == input2:
    print("Equal!")
elif input1 < input2:
    print(f"{input2} is greater than {input1}")
else:
    print(f"{input1} is greater than {input2}")

input3 = int(input("Enter a number between 0 and 10: "))
while input3 < 0 or 10 < input3:
    input3 = int(input("Enter a number between 0 and 10: "))
else:
    print("Congratulations!")
