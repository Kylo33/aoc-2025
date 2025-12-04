from collections import Counter, defaultdict, deque
import heapq

import sys
text = sys.stdin.read().strip()
grid = text.split('\n')

ans = 0

deltas = []
for x in range(-1, 2):
    for y in range(-1, 2):
        if x or y:
            deltas.append((x, y))

q = deque()
seen = set()
papers = {}

for r in range(len(grid)):
    for c in range(len(grid[0])):
        count = 0
        for dr, dc in deltas:
            if 0 <= r + dr < len(grid) and 0 <= c + dc < len(grid[0]):
                if grid[r + dr][c + dc] == '@':
                    count += 1
                    papers[(r, c)] = count

        if count < 4 and grid[r][c] == '@':
            q.append((r, c))

ans = 0
while q:
    r, c = q.popleft()
    if (r, c) in seen:
        continue
    seen.add((r, c))
    ans += 1
    for dr, dc in deltas:
        if 0 <= r + dr < len(grid) and 0 <= c + dc < len(grid[0]):
            if grid[r + dr][c + dc] == '@':
                papers[(r + dr, c + dc)] -= 1
                if papers[(r + dr, c + dc)] < 4:
                    q.append((r + dr, c + dc))

print(ans)
