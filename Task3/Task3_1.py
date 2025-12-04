

with open("Task3/input.txt", encoding="utf-8") as file:
    data = file.read()
    banks_table = data.split("\n")
    banks_table = [[int(i) for i in bank] for bank in banks_table]


batteries = []
for bank in banks_table:
    max_ids = [0 for _ in range(12)]
    max_current = [0 for _ in range(12)]
    for k in range(12):
        last_max = 0 if k == 0 else max_ids[k-1] + 1
        if k == 11:
            start_id = max(k, last_max)
            for i, battery in enumerate(bank[start_id:]):
                if battery > max_current[k]:
                    max_ids[k] = i + last_max
                    max_current[k] = battery
                if max_current[k] == 9:
                    break
            # print(max_current, max_ids)
        else:
            start_id = max(k, last_max)
            for i, battery in enumerate(bank[start_id:(100-(11-k))]):
                if battery > max_current[k]:
                    max_ids[k] = i + last_max
                    max_current[k] = battery
                if max_current[k] == 9:
                    break
            # print(max_current, max_ids)
    joltage = sum([battery * (10 ** (11-k)) for k, battery in enumerate(max_current)])
    batteries.append(joltage)

print(batteries)
print(sum(batteries))