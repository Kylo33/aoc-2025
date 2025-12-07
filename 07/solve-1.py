from collections import Counter, defaultdict, deque
import heapq

import sys
text = sys.stdin.read().strip()
grid = [list(line) for line in text.split('\n')]

deltas_4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
deltas_8 = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

def print_grid():
    for line in grid:
        print(*line,sep="")

ans = 0
for i, line in enumerate(grid[:-1]):
    for j, cell in enumerate(line):
        if cell == '|' or cell == 'S':
            if grid[i+1][j] == '^':
                grid[i + 1][j-1] = '|'
                grid[i + 1][j+1] = '|'
                ans += 1
            else:
                grid[i+1][j] = '|'
    print_grid()

print(ans)
