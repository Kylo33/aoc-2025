from collections import Counter, defaultdict, deque
from functools import reduce
from math import sqrt
import heapq

import sys
text = sys.stdin.read().strip()
grid = [list(line) for line in text.split('\n')]
times = int(text.split('\n')[0]) # I modified the input to have the number of edges to connect on the first line
lines = text.split('\n')[1:]

deltas_4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
deltas_8 = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

adj = defaultdict(list)
edges = []

for i in range(len(lines)):
    for j in range(i + 1, len(lines)):
        x1, y1, z1 = map(int, lines[i].split(','))
        x2, y2, z2 = map(int, lines[j].split(','))
        dist = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
        heapq.heappush(edges, (dist, i, j))

for _ in range(times):
    dist, i, j = heapq.heappop(edges)
    adj[i].append(j)
    adj[j].append(i)


seen = set()

sizes = []
for x in adj:
    def dfs(x):
        if x in seen:
            return 0
        seen.add(x)
        return 1 + sum(dfs(y) for y in adj[x])
    sizes.append(dfs(x))

sizes.sort(reverse=True)
print(reduce(lambda x, y: x * y, sizes[:3]))
