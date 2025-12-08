import numpy as np
import math
import pandas as pd
import os
import time
from termcolor import colored
from collections import Counter
import scipy

with open("Task8/input_test.txt", encoding="utf-8") as file:
    data = file.read()
    junction_boxes = data.split("\n")

junction_boxes_coords = []
for k, jb in enumerate(junction_boxes):
    coords = [int(i) for i in jb.split(',')]
    junction_boxes_coords.append(coords)

def distance3d(point1: list, point2: list) -> float:
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    dist = np.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2) + ((z1 - z2) ** 2))
    return float(dist)

junction_boxes_array = np.array(junction_boxes_coords)
jb_tree = scipy.spatial.cKDTree(junction_boxes_array)
jb_assigned = []
for i, coords in enumerate(junction_boxes_array):
    neighbor = jb_tree.query(coords, k=2)
    neighbor_dist, neighbor_id = float(neighbor[0][1]), int(neighbor[1][1])
    print(f'For point {coords} found neighbor {neighbor_id} in distance {neighbor_dist: 10.2f}')
    jb_assigned.append([neighbor_id, neighbor_dist, i, i, f'{min(neighbor_id, i)}-{max(neighbor_id, i)}'])

jb_assigned_sorted = sorted(jb_assigned, key=lambda x : x[1])

cuircuit_id = 0
handled_junkboxes = set()
for i in range(len(jb_assigned_sorted)):
    if len(handled_junkboxes) == 10:
        break

    neighbor_id, neighbor_dist, current_id, current_cuircuit, current_name = jb_assigned_sorted[i]
    n_of_n_id, _, _, neighbor_cuircuit, _ = jb_assigned[neighbor_id]
    if current_name in handled_junkboxes:
        continue
    handled_junkboxes.add(current_id)
    if n_of_n_id == current_id:
        handled_junkboxes.add(neighbor_id)
    if neighbor_cuircuit == current_cuircuit:
        print(f'Current point: {current_id}. Closest neighbor: {neighbor_id}. Already in the same cuircuit: {current_cuircuit}')
    else:
        new_cuircuit = min(neighbor_cuircuit, current_cuircuit)
        print(f'Current point: {current_id}. Closest neighbor: {neighbor_id}. Assigned to cuircuit: {new_cuircuit}')
        for j in range(len(jb_assigned_sorted)):
            this_cuircuit = jb_assigned[j][3]
            if this_cuircuit == neighbor_cuircuit or this_cuircuit == current_cuircuit:
                jb_assigned[j][3] = new_cuircuit          
    jb_assigned_sorted = sorted(jb_assigned, key=lambda x : x[1])

jb_assigned_sorted = sorted(jb_assigned, key=lambda x : x[1])
for jb in jb_assigned:
    print(jb)
data = Counter([item[3] for item in jb_assigned])
print(data.most_common(10))