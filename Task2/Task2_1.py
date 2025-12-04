from itertools import groupby

def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

with open("Task2/input.txt", encoding="utf-8") as file:
    data = file.read()
    ranges_table_v1 = data.split(",")
    ranges_table = [[int(x) for x in my_range.split("-")] for my_range in ranges_table_v1]

invalid_ids = {str(x)+"-"+str(y): set() for x,y in ranges_table}
result = set()

divisors = [[] for i in range(51)]
for i in range(2, 51):
    for j in range(2,i+1):
        if i % j == 0:
            divisors[i].append(j)

for ranges in ranges_table:
    # print(ranges)
    start = ranges[0]
    end = ranges[1]
    start_len = len(str(start))
    end_len = len(str(end))
    for id in range(start, end+1, 1):
        id_len = len(str(id))
        for d in divisors[id_len]:
            divided = id_len // d
            fragments = [str(id)[k*divided:(k+1)*divided] for k in range(d)]
            if all_equal(fragments):
                print(fragments)
                # print(f"For divisor {d} we found {id}")
                invalid_ids[str(start)+"-"+str(end)].add(id)
                result.add(id)

print(invalid_ids)
print(sum(result))
print(divisors)
31600153442