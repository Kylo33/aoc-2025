from collections import Counter, defaultdict, deque
import heapq

import sys
text = sys.stdin.read().strip()
grid = [list(line) for line in text.split('\n')]

deltas_4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
deltas_8 = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

beams = [[0] * len(grid[0]) for _ in range(len(grid))]
for i in range(len(beams[0])):
    if grid[0][i] == 'S':
        beams[0][i] = 1

for i, line in enumerate(grid[:-1]):
    for j, cell in enumerate(line):
        if grid[i+1][j] == '^':
            beams[i+1][j+1] += beams[i][j]
            beams[i+1][j-1] += beams[i][j]
        else:
            beams[i+1][j] += beams[i][j]

print(sum(beams[-1]))
