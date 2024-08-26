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
tenths = {name: tenth for name, count in stock.items() if (tenth := count // 10) > 0}
print(tenths)

tenths = {}
for name, count in stock.items():
    if (tenth := count // 10) > 0:
        tenths[name] = tenth

print(tenths)
