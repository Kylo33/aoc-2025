from collections import Counter, defaultdict, deque
import heapq

import sys
text = sys.stdin.read().strip()
grid = [list(line) for line in text.split('\n')]

ans = 0

deltas = []
for x in range(-1, 2):
    for y in range(-1, 2):
        if x or y:
            deltas.append((x, y))

while True:
    changed = False
    new_grid = [line[:] for line in grid]
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            count = 0
            for dr, dc in deltas:
                if 0 <= r + dr < len(grid) and 0 <= c + dc < len(grid[0]):
                    if grid[r + dr][c + dc] == '@':
                        count += 1

            if count < 4 and grid[r][c] == '@':
                new_grid[r][c] = '.'
                ans += 1
                changed = True
    if not changed:
        break
    grid = new_grid

print(ans)
