import numpy as np
import math
import pandas as pd
import os
import time

with open("Task7/input.txt", encoding="utf-8") as file:
    data = file.read()
    diagram = data.split("\n")

def find_characters(given_list: list, char:str) -> list:
    return [p for p, c in enumerate(given_list) if c == char]

def print_diagram(diagram: list, splits: list) -> None:
    os.system('clear')
    for i, line in enumerate(diagram):
        print(''.join(line), splits[i])

def split_beam(ids: list, previous_beams: list) -> tuple:
    new_line = set()
    no_of_splits = 0
    for item in ids:
        if item in previous_beams:
            new_line.add(item-1)
            new_line.add(item+1)
            no_of_splits += 1
    continued_beams = set(previous_beams).difference(set(ids))
    final_line = sorted(list(new_line.union(continued_beams)))
    return no_of_splits, final_line

number_of_splits = 0
new_diagram = []
no_of_splits = [0]
for i, line in enumerate(diagram):
    if i == 0:
        where_draw = find_characters(line, 'S')
        new_line = line
    else:
        splitters = find_characters(line, '^')
        if splitters == []:
            splits = 0
        else:
            splits, where_draw = split_beam(splitters, where_draw)
        
        temp = ['|' if p in where_draw else c for p, c in enumerate(line) ]
        new_line = ''.join(temp)
        no_of_splits.append(splits)
    
    new_diagram.append(new_line)
    print_diagram(new_diagram, no_of_splits)
    time.sleep(0.5)

print(sum(no_of_splits))