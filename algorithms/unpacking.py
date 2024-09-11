"""The catch-all unpacking"""

# sample list data
sorted_ages = [12, 15, 17, 24, 25, 26, 27, 28, 30, 42]

# indexing - it still works
youngest = sorted_ages[0]
second_youngest = sorted_ages[1]
others = sorted_ages[2:]

# catch-all unpacking
youngest, second_youngest, *others = sorted_ages

# catch-all can be anywhere in your statement
youngest, *others, oldest = sorted_ages

*others, second_oldest, oldest = sorted_ages


# you can't use multiple catch-all in a statement
# first, *middle, *second_middle, last = [1, 2, 3, 4]

# another use-case in CSVs
# header, *rows = ["name,age", "Emmah,30"]


# catch-all as a function parameter
def log(*args):  # take any number of positional args
    print(args)
