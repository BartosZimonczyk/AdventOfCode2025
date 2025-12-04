import numpy 
import math

with open("Task1/input.txt", encoding="utf-8") as file:
    data = file.read()
    code_table = data.split("\n")

current_position = 50
times_at_zero = 0
for code in code_table:
    # print(code)
    if len(code) < 2:
        pass
    else:
        direction = code[0]
        distance = int(code[1:])
        for _ in range(distance):
            if direction == 'L':
                current_position = (current_position - 1) % 100
            elif direction == 'R':
                current_position = (current_position + 1) % 100
            else:
                pass
            if current_position == 0:
                times_at_zero += 1

print(times_at_zero)