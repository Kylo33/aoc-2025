from collections import Counter, defaultdict, deque
import sys
from math import sqrt
import heapq

# 👀 Um... this is needed
import sys
sys.setrecursionlimit(9999)

text = sys.stdin.read().strip()
grid = [list(line) for line in text.split('\n')]
lines = text.split('\n')[1:] # In part 1, I put the number of edges on the first line

deltas_4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
deltas_8 = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

adj = defaultdict(set)
edges = []

for i in range(len(lines)):
    for j in range(i + 1, len(lines)):
        x1, y1, z1 = map(int, lines[i].split(','))
        x2, y2, z2 = map(int, lines[j].split(','))
        dist = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
        heapq.heappush(edges, (dist, i, j))
      
ans = []

def count_size(source, seen):
    if source in seen:
        return 0
    seen.add(source)
    return 1 + sum(count_size(dest, seen) for dest in adj[source])

# This is O(n^3), runs in about 4 seconds.
while True:
    dist, i, j = heapq.heappop(edges)
    adj[i].add(j)
    adj[j].add(i)
    ans = [i, j]
    if count_size(i, set()) == len(lines):
        break

f, s = map(lambda x: int(lines[x].split(',')[0]), ans)
print(f * s)
