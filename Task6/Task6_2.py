import numpy as np
import math
import pandas as pd

with open("Task6/input.txt", encoding="utf-8") as file:
    data = file.read()
    homework = data.split("\n")

homework_operations = homework[-1].split(" ")
homework_operations = [e for e in homework_operations if e != '']

def find_characters(given_list: list, char:str) -> list:
    return [p for p, c in enumerate(given_list) if c == char]

def common_elemets(list1: list, list2: list) -> list:
    return list(set(list1).intersection(set(list2)))

def ce_all(given_list: list) -> list:
    n = len(given_list)
    flat_list = []
    
    for xs in given_list:
        for x in xs:
            flat_list.append(x)
    
    current_common_elements = flat_list.copy()
    for i in range(n):
        current_common_elements = common_elemets(current_common_elements, given_list[i])
    
    current_common_elements.append(0)
    return sorted(current_common_elements)

def group_vertical_numbers(given_list: list) -> list:
    n_of_numbers = len(given_list)
    n_of_tasks = len(given_list[0])

    final_list = []
    for i in range(n_of_tasks):
        l = len(given_list[0][i])
        current_task_numbers = []
        for k in range(l):
            current_number = []
            for j in range(n_of_numbers):
                current_symbol = given_list[j][i][k]
                if current_symbol != ' ':
                    current_number.append(current_symbol)
            current_task_numbers.append(''.join(current_number))
        final_list.append([int(n) for n in current_task_numbers if n != ''])

    return final_list

where_spaces = [find_characters(line, " ") for line in homework[:-1]]
common_spaces = ce_all(where_spaces)
common_spaces.append(None)
homework_numbers = [[line[common_spaces[i]:common_spaces[i+1]] for i in range(len(common_spaces)-1)] for line in homework[:-1]]

# print(homework_numbers)
new_numbers = group_vertical_numbers(homework_numbers)
# print(new_numbers)

solutions = [0 for _ in range(len(homework_operations))]
final_sum = 0

for i, operation in enumerate(homework_operations):
    line = new_numbers[i]
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

# print(solutions)
print(final_sum)
