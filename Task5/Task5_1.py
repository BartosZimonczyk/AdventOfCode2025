import numpy as np
import math

with open("Task5/input_test.txt", encoding="utf-8") as file:
    data = file.read()
    ranges, ingridients = data.split("\n\n")

ranges = [row.split("-") for row in ranges.split("\n")]
ranges = np.array(ranges, dtype=int)
ingridients = set([int(row) for row in ingridients.split("\n")])

fresh_amount = 0
min_range = np.min(ranges[:,0])
max_range = np.max(ranges[:,1])
for start, end in ranges:
    print(f"working on range {start} - {end}...    ")
    fresh_amount += end-start

print(fresh_amount)