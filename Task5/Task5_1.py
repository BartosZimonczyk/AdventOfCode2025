import numpy as np
import math

with open("Task5/input.txt", encoding="utf-8") as file:
    data = file.read()
    ranges, ingridients = data.split("\n\n")

ranges = [row.split("-") for row in ranges.split("\n")]
ranges = np.array(ranges, dtype=int)
ingridients = set([int(row) for row in ingridients.split("\n")])


min_range = np.min(ranges[:,0])
max_range = np.max(ranges[:,1])
ranges_sorted = ranges[ranges[:, 0].argsort()]

fresh_items_found = []
fresh_amount = 0
previous_end = ranges_sorted[0, 0]
for start, end in ranges_sorted:

    print(f"Working on range {start} - {end}...", end=" ")
    if end < start:
        print("XDDD")
        continue

    no_of_ids = 0
    if end <= previous_end:
        print("")
        continue
    if start < previous_end:
        start = previous_end
        print(f"Moved start to {start}...", end=" ")
    else:
        no_of_ids += 1
    
    no_of_ids += end-start
    fresh_amount += no_of_ids
    fresh_items_found.append(no_of_ids)
    previous_end = end
    print(f"Found {no_of_ids} fresh items.")


print(fresh_amount)
print(sum(fresh_items_found))