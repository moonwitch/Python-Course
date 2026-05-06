###############################################################################
# EXERCISE 1:
# List comprehension syntax: [expression for item in iterable]
###############################################################################
numbers = [1, 2, 3, 4, 5]

print([n**2 for n in numbers])
"""
Lambda version list(map(lambda n: n**2, numbers))
- List Comprehension is far easier to read and understand
- List Comprehension also doesn't require the list() wrapper to print, since
you can not print map() straight away.
"""
###############################################################################
# EXERCISE 2:
###############################################################################
funzies = [-2, -4, 1, 0, -3, -7, -8, 5, 9, 1, -2]

# print(filter([n >= 0 for n in funzies])) Nope -> filtering happens after;
# so this needs to be reversed
print([n for n in funzies if n >= 0])
###############################################################################
# EXERCISE 3:
###############################################################################
nonfunzies = [-2, -4, 1, 0, -3, -7, -8, 5, 9, 1, -2]

print([n for n in nonfunzies if n % 2 != 0])
