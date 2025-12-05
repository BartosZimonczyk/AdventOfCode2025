import numpy as np
import math

with open("Task4/input.txt", encoding="utf-8") as file:
    data = file.read()
    matrix = data.split("\n")
    matrix = np.matrix([[item for item in row] for row in matrix], dtype=str)

n_rows, n_cols = matrix.shape

def get_neighbors(row, col):
    return [(row-1, col-1),
            (row-1, col),
            (row-1, col+1),
            (row, col-1),
            (row, col+1),
            (row+1, col-1),
            (row+1, col),
            (row+1, col+1)]

removed_papers = 0
removed_this_iteration = 1

while removed_this_iteration > 0:
    removed_this_iteration = 0
    new_matrix = np.zeros(shape=(n_rows, n_cols), dtype=str)
    for row in range(n_rows):
        for col in range(n_cols):
            neighbors = get_neighbors(row, col)
            if matrix[row, col] == "@":
                count = 0
                for r, c in neighbors:
                    if r > -1 and c > -1 and r < n_rows and c < n_cols:
                        if matrix[r, c] == "@":
                            count += 1
                if count < 4:
                    removed_papers +=1
                    removed_this_iteration += 1
                    new_matrix[row, col] = "."
                else:
                    new_matrix[row, col] = "@"
            else:
                new_matrix[row, col] = "."
    matrix = new_matrix.copy()


with open("Task4/output.txt", "w") as output:
    for row in range(n_rows):
        new_row = "".join(new_matrix[row])
        output.write(new_row + "\n")

print(removed_papers)