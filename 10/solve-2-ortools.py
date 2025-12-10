from collections import Counter, defaultdict, deque
import heapq
from ortools.init.python import init
from ortools.linear_solver import pywraplp

import sys
text = sys.stdin.read().strip()
grid = [list(line) for line in text.split('\n')]
lines = text.split("\n")

deltas_4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
deltas_8 = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

ans = 0
for line in lines:
    parts = line.split(" ")
    target = list(map(int, parts[-1][1:-1].split(',')))

    target_btns = [[] for _ in range(len(target))]
    solver = pywraplp.Solver.CreateSolver("CBC")
    vars = []

    for i, button_part in enumerate(parts[1:-1]):
        vars.append(solver.IntVar(0, solver.infinity(), str(i)))
        button_targets = list(map(int, button_part[1:-1].split(",")))
        for target_val in button_targets:
            target_btns[target_val].append(vars[-1])

    for target_btn_list, target_val in zip(target_btns, target):
        solver.Add(sum(target_btn_list) == target_val)

    solver.Minimize(sum(vars))
    solver.Solve()
    ans += sum(var.solution_value() for var in vars)

print(round(ans))
