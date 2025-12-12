from collections import Counter, defaultdict, deque
import heapq

# from ortools.init.python import init
# from ortools.linear_solver import pywraplp
# solver = pywraplp.Solver.CreateSolver("CBC")

import sys
text = sys.stdin.read().strip()
grid = [list(line) for line in text.split('\n')]
lines = text.split("\n")

deltas_4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
deltas_8 = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
