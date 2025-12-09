from collections import Counter, defaultdict, deque
import sys
from math import sqrt
import heapq

text = sys.stdin.read().strip()
grid = [list(line) for line in text.split('\n')]
lines = text.split('\n')[1:] # In part 1, I put the number of edges on the first line
points = [tuple(map(int, line.split(','))) for line in lines]

deltas_4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
deltas_8 = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

class Node:
    def __init__(self, parent, size, point):
        self.parent=parent
        self.size=size
        self.point=point

    def __str__(self):
        parent,size,point=self.parent,self.size,self.point
        return f"Node({parent=},{size=},{point=})"

adj = defaultdict(set)
edges = []

def dist(p1, p2):
    x1, y1, z1 = p1.point
    x2, y2, z2 = p2.point
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
    

nodes = [Node(None, 1, point) for point in points]
for i in range(len(nodes)):
    for j in range(i + 1, len(nodes)):
        d=dist(nodes[i], nodes[j])
        heapq.heappush(edges, (d, i, j))

def unite(i: Node, j: Node):
    rep_1 = i
    while rep_1.parent is not None:
        rep_1 = rep_1.parent

    rep_2 = j
    while rep_2.parent is not None:
        rep_2 = rep_2.parent

    if rep_1 == rep_2:
        return

    if rep_1.size < rep_2.size:
        rep_1.parent = rep_2
        rep_2.size += rep_1.size
    else:
        rep_2.parent = rep_1
        rep_1.size += rep_2.size

def get_size(i: Node):
    rep = i
    while rep.parent is not None:
        rep = rep.parent

    return rep.size


ans = 0
while True:
    dist, i, j = heapq.heappop(edges)
    i, j = nodes[i], nodes[j]
    unite(i,j)
    ans = i.point[0]*j.point[0]
    if get_size(j) == len(lines):
        break

print(ans)
