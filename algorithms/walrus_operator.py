"""
Use walrus operator (:=) to avoid repeat work.
Note:
The walrus operator was introduced in Python 3.8
"""

stock = {
    "dresses": 125,
    "pants": 200,
    "dresses": 300,
    "bags": 24,
}

# get how many tenths there are in stock counts
# using dict comprehensions
tenths = {name: tenth for name, count in stock.items() if (tenth := count // 10) > 0}
print(tenths)

# using traditional loops
# the following code is the same as the code above
tenths = {}  # create an empty dict
for name, count in stock.items():
    if (tenth := count // 10) > 0:
        tenths[name] = tenth  # add pairs to dict

print(tenths)
