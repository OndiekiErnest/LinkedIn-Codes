"""
Use comprehensions instead of `map` and `filter`
because comprehensions are easier to read for simple tasks.
`map` needs a `lambda` function, which can make the code look cluttered.
"""

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# get the squares of numbers that are divisible by 2
# much harder to read
even_squares = map(lambda x: x**2, filter(lambda x: x % 2 == 0, data))
print(even_squares)
# Output: [4, 16, 36, 64, 100]

# much easier to read
even_squares = [x**2 for x in data if (x % 2 == 0)]
print(even_squares)
# Output: [4, 16, 36, 64, 100]
