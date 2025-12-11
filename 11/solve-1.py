from collections import Counter, defaultdict, deque
import heapq
from functools import cache

# from ortools.init.python import init
# from ortools.linear_solver import pywraplp
# solver = pywraplp.Solver.CreateSolver("CBC")

import sys
text = sys.stdin.read().strip()
grid = [list(line) for line in text.split('\n')]
lines = text.split("\n")

deltas_4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
deltas_8 = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

# topo sort
nodes = set()

adj = defaultdict(list)
for line in lines:
    parts = line.split(" ")
    src = parts[0][:-1]
    nodes.add(src)
    for dest in parts[1:]:
        nodes.add(dest)
        adj[src].append(dest)

@cache
def ways_out(node):
    if node == "out":
        return 1
    return sum(ways_out(other_node) for other_node in adj[node])

print(ways_out("you"))

