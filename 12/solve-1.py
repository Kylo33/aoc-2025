from collections import Counter, defaultdict, deque
import heapq

from ortools.sat.python import cp_model

import sys
text = sys.stdin.read().strip()
grid = [list(line) for line in text.split('\n')]

deltas_4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
deltas_8 = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

shapes = []
*shape_strs, requirements = text.split("\n\n")
for shape in shape_strs:
    these_shapes = []
    shape = shape.split("\n")[1:]
    shape_l=[]
    for r in range(len(shape)):
        for c in range(len(shape[0])):
            if shape[r][c] == '#':
                shape_l.append([r, c])
    these_shapes.append(shape_l)
    for i in range(3):
        shape = list(zip(*shape[::-1]))
        shape_l=[]
        for r in range(len(shape)):
            for c in range(len(shape[0])):
                if shape[r][c] == '#':
                    shape_l.append([r, c])
        these_shapes.append(shape_l)
    shapes.append(these_shapes)

ans = 0
solver = cp_model.CpSolver()
for time,requirement in enumerate(requirements.split("\n")):
    width, height = map(int, requirement.split(":")[0].split("x"))
    model = cp_model.CpModel()
    grid = [[[] for _ in range(width)] for _ in range(height)]

    shape_requirements = list(map(int, requirement.split(": ")[1].split()))

    for i in range(len(shapes)):
        shape_vars = []
        for r in range(len(grid)-2):
            for c in range(len(grid[0])-2):
                for j in range(len(shapes[i])):
                    var = model.new_int_var(0, 1, str((r,c,i,j)))
                    for dr, dc in shapes[i][j]:
                        grid[r+dr][c+dc].append(var)
                    shape_vars.append(var)

        count = shape_requirements[i]
        model.add(sum(shape_vars) == count)

    for row in grid:
        for col_list in row:
            model.add(sum(col_list) <= 1)
            model.add(sum(col_list) >= 0)


    print(f"calling solve, {time=}")
    status = solver.solve(model)
    print(status != cp_model.INFEASIBLE)
    if status != cp_model.INFEASIBLE:
        ans += 1

print(ans)
    
