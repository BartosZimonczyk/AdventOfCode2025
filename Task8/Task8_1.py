import numpy as np
import math
import pandas as pd
import os
import time
from termcolor import colored

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

jb_with_assignments.sort(key = lambda x: x[2])
for jb in jb_with_assignments:
    print(jb)

managed_connections = []
for i in range(len(jb_with_assignments)):
    first_jb, first_ass, first_dist, first_neighbor, first_id = jb_with_assignments[i]
    
        
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
    # if first_ass == min_ass:
    #     print(f"Closest neighbor is point no. {min_point}. Both are already assigned to circuit no. {first_ass}")
    # elif first_ass != min_ass:
    #     new_id = min(first_ass, min_ass)
    #     print(f"Closest neighbor is point no. {min_point}. Both are already assigned different ciruits. Merging {first_ass} and {min_ass} to {new_id}")
    #     for j in range(len(jb_with_assignments)):
    #         second_jb, second_ass = jb_with_assignments[j]
    #         if second_ass == min_ass:
    #             jb_with_assignments[j][1] = new_id
    
# print(jb_with_assignments)