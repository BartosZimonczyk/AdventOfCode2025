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
jb_assigned = dict()
cuircuit_names = set()
for i, coords in enumerate(junction_boxes_array):
    neighbors = jb_tree.query(coords, k=20)
    for j in range(len(neighbors[0])):
        if j == 0:
            continue
        neighbor_dist, neighbor_id = float(neighbors[0][j]), int(neighbors[1][j])
        cuircuit_name = f'{min(neighbor_id, i)}-{max(neighbor_id, i)}'
        if cuircuit_name in cuircuit_names:
            continue
        cuircuit_names.add(cuircuit_name)
            
        print(f'For point {coords} found neighbor {neighbor_id} in distance {neighbor_dist: 10.2f}')
        # if cuircuit_name not in cuircuit_names:
        jb_assigned[cuircuit_name] = [str(neighbor_id), neighbor_dist, set([i])]
        cuircuit_names.add(cuircuit_name)

jb_assigned_sorted = dict(sorted(jb_assigned.items(), key=lambda kv : kv[1][1]))
cuircuit_id = 0
handled_cuircuits = set()
keys_sorted = [kv for kv in jb_assigned_sorted]

for jb in jb_assigned_sorted.items():
    print(jb)

for i, key in enumerate(keys_sorted):
    if i == 10:
        break

    neighbor_id, neighbor_dist, current_cuircuit = jb_assigned_sorted[key]
    n_of_n_id, _, neighbor_cuircuit = jb_assigned[neighbor_id]

    if neighbor_cuircuit == current_cuircuit:
        print(f'Current point: {key}. Closest neighbor: {neighbor_id}. Already in the same cuircuit: {current_cuircuit}')
    else:
        new_cuircuit = neighbor_cuircuit | current_cuircuit
        print(f'Current point: {key}. Closest neighbor: {neighbor_id}. Assigned to cuircuit: {new_cuircuit}')
        for key_loop in keys_sorted:
            this_cuircuit = jb_assigned[key_loop][2]
            if this_cuircuit == neighbor_cuircuit or this_cuircuit == current_cuircuit:
                jb_assigned[key_loop][2] = new_cuircuit          
    jb_assigned_sorted = dict(sorted(jb_assigned.items(), key=lambda kv : kv[1][1]))

jb_assigned_sorted = dict(sorted(jb_assigned.items(), key=lambda kv : kv[1][1]))
for jb in jb_assigned_sorted.items():
    print(jb)

data = Counter(['_'.join(sorted([str(v) for v in item[2]])) for key, item in jb_assigned.items()])
print(data.most_common(10))