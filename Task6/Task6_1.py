import numpy as np
import math
import pandas as pd

with open("Task6/input.txt", encoding="utf-8") as file:
    data = file.read()
    homework = data.split("\n")

homework = [line.split(" ") for line in homework]
homework = [[e for e in line if e != ''] for line in homework]
homework_numbers = [[int(e) for e in line] for line in homework[:-1]]
homework_operations = homework[-1]
homework_matrix = np.matrix(homework_numbers).T

solutions = [0 for _ in range(len(homework_operations))]
final_sum = 0

for i, operation in enumerate(homework_operations):
    line = homework_matrix[i, :].tolist()[0]
    print(f"{i}. Solving {operation} problem for numbers {line}...", end=" ")

    if operation == '+':
        solution = 0
        for number in line:
            solution = solution + number
    elif operation == '*':
        solution = 1
        for number in line:
            solution = solution * number
    
    print(f"Solution for this line is {solution}.")
    solutions[i] = solution
    final_sum += solution

print(solutions)
print(final_sum)
