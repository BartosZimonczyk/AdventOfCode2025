import numpy as np
import math
import pandas as pd
import os
import time
from termcolor import colored

with open("Task7/input.txt", encoding="utf-8") as file:
    data = file.read()
    diagram = data.split("\n")

def find_characters(given_list: list, char:str) -> list:
    return [p for p, c in enumerate(given_list) if c == char]

def print_diagram(diagram: list, diagram_timelines: list) -> None:
    os.system('clear')
    for i, line in enumerate(diagram):
        print(''.join(line), sum(diagram_timelines[i]))

def print_timelines(diagram: list) -> None:
    for i, line in enumerate(diagram):
        print(*[colored(item, 'white') if item == 0 else colored(item, 'red') for item in line])

def split_beam(ids: list, previous_beams: list, previous_counted_beams: list) -> tuple:
    new_line = set()
    no_of_splits = 0
    counted_beams = [0 if i in ids else previous_counted_beams[i] for i, k in enumerate(previous_counted_beams)]
    for item in ids:
        if item in previous_beams:
            new_line.add(item-1)
            new_line.add(item+1)
            
            counted_beams[item-1] += previous_counted_beams[item]
            counted_beams[item+1] += previous_counted_beams[item]
            
            no_of_splits += 1
           
    continued_beams = set(previous_beams).difference(set(ids))
    final_line = sorted(list(new_line.union(continued_beams)))
    return no_of_splits, final_line, counted_beams

number_of_splits = 0
new_diagram = []
new_diagram_count = []
no_of_splits = [0]
for i, line in enumerate(diagram):
    if i == 0:
        where_draw = find_characters(line, 'S')
        new_line = line
        new_diagram_count = [[0 if c == '.' else 1 for c in new_line]]
    else:
        splitters = find_characters(line, '^')
        if splitters == []:
            splits = 0
            counted_beams = new_diagram_count[-1]
        else:
            splits, where_draw, counted_beams = split_beam(splitters, where_draw, new_diagram_count[-1])
        
        temp = ['|' if p in where_draw else c for p, c in enumerate(line)]
        new_line = ''.join(temp)
        new_diagram_count.append(counted_beams)
        no_of_splits.append(splits)
    
    new_diagram.append(new_line)
    print_diagram(new_diagram, new_diagram_count)
    print_timelines(new_diagram_count)
    
    # time.sleep(0.1)

print(sum(new_diagram_count[-1]))