import numpy as np
import math
import pandas as pd
import os
import time
from termcolor import colored
from collections import Counter

with open("Task8/input_test.txt", encoding="utf-8") as file:
    data = file.read()
    junction_boxes = data.split("\n")

jb_with_assignments = []
for k, jb in enumerate(junction_boxes):
    coords = [int(i) for i in jb.split(',')]
    jb_with_assignments.append([coords, k, -1, -1, ''])

def distance3d(point1: list, point2: list) -> float:
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    dist = np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
    return float(dist)

circuiut_id = 0
for i in range(len(jb_with_assignments)):
    first_jb, first_ass, first_dist, first_neighbor, first_id = jb_with_assignments[i]
    distances_to_all = []
    min_distance = -1
    min_ass = -1
    min_point = -1
    for j in range(len(jb_with_assignments)):
        if i == j:
            continue
        
        second_jb, second_ass, second_dist, second_neighbor, second_id = jb_with_assignments[j]
        dist = distance3d(first_jb, second_jb)
        
        if j == 0 or (i == 0 and j == 1):
            min_distance, min_ass, min_point = dist, second_ass, j
        else:
            if dist < min_distance:
                min_distance, min_ass, min_point = dist, second_ass, j
    
    jb_with_assignments[i][2] = min_distance
    jb_with_assignments[i][3] = min_point
    jb_with_assignments[i][4] = f'{min(i, min_point)}_{max(i, min_point)}'

jb_with_assignments_sorted = sorted(jb_with_assignments, key = lambda x: x[2])
for jb in jb_with_assignments_sorted:
    print(jb)

managed_connections = set()
circuiut_id = 0
for i in range(len(jb_with_assignments_sorted)):
    jb_with_assignments_sorted = sorted(jb_with_assignments, key = lambda x: x[2])
    first_jb, first_ass, first_dist, first_neighbor, first_id = jb_with_assignments_sorted[i]
    if first_id in managed_connections:
        continue

    managed_connections.add(first_id)

    second_jb, second_ass, second_dist, second_neighbor, second_id = jb_with_assignments[first_neighbor]
    
    # if first_ass == -1 and min_ass == -1:
    #     print(f"Closest neighbor is point no. {min_point}. Both assigned to new circuit no. {circuiut_id}")
    #     jb_with_assignments[i][1] = circuiut_id
    #     jb_with_assignments[min_point][1] = circuiut_id
    #     circuiut_id +=1
    # elif min_ass == -1:
    #     print(f"Closest neighbor is point no. {min_point}. Neighbor assigned to existing circuit no. {first_ass}")
    #     jb_with_assignments[min_point][1] = first_ass
    # elif first_ass == -1:
    #     print(f"Closest neighbor is point no. {min_point}. Current box assigned to existing circuit no. {min_ass}")
    #     jb_with_assignments[i][1] = min_ass
    if first_ass == second_ass:
        print(f"Both are already assigned to circuit no. {first_ass}")
    elif first_ass != second_ass:
        new_id = min(first_ass, second_ass)
        print(f"Both are assigned different ciruits. Merging {first_ass} and {second_ass} to {new_id}")
        for j in range(len(jb_with_assignments)):
            third_jb, third_ass, third_dist, third_neighbor, third_id = jb_with_assignments[j]
            if third_ass == second_ass:
                jb_with_assignments[j][1] = new_id
    
    if len(managed_connections) == 10:
        break

data = Counter([item[1] for item in jb_with_assignments])

print(data.most_common(10))