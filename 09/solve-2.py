from collections import Counter, defaultdict, deque
import heapq

import sys
text = sys.stdin.read().strip()
grid = [list(line) for line in text.split('\n')]
lines = text.split("\n")

deltas_4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
deltas_8 = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

points = list(map(lambda x: tuple(map(int, x.split(","))), lines))


w = len(set(map(lambda p: p[0], points)))
h = len(set(map(lambda p: p[1], points)))

grid = [[False] * w for _ in range(h)]

# map coordinates in points to coodinates in grid
xs = list(set(map(lambda p: p[0], points)))
xs.sort()
x_map = {x: i for i, x in enumerate(xs)}
x_map_rev = {i: x for i, x in enumerate(xs)}
ys = list(set(map(lambda p: p[1], set(points))))
ys.sort()
y_map = {y: i for i, y in enumerate(ys)}
y_map_rev = {i: y for i, y in enumerate(ys)}

for i in range(len(points)):
    j = (i + 1) % len(points)
    x1, y1 = [x_map[points[i][0]], y_map[points[i][1]]]
    x2, y2 = [x_map[points[j][0]], y_map[points[j][1]]]

    for x in range(min(x1,x2), max(x1,x2)+1):
        for y in range(min(y1,y2),max(y1,y2)+1):
            grid[y][x] = True

seen = set()
queue = deque([(30,100)])
while queue:
    x, y = queue.popleft()
    if (x, y) in seen:
        continue
    seen.add((x,y))
    for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
        if not grid[x+dx][y+dy]:
            queue.append((x+dx,y+dy))

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (i, j) in seen:
            grid[i][j] = True

ans = 0
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        x1,y1=points[i]
        x2,y2=points[j]

        mx1,mx2=x_map[x1],x_map[x2]
        my1,my2=y_map[y1],y_map[y2]

        works = True
        for x in range(min(mx1,mx2),max(mx1,mx2)+1):
            if not grid[my1][x] or not grid[my2][x]:
                works = False
                
        for y in range(min(my1,my2),max(my1,my2)+1):
            if not grid[y][mx1] or not grid[y][mx2]:
                works = False

        if works:
            area = (abs(x1-x2)+1)*(abs(y1-y2)+1)
            ans = max(ans, area)

print(ans)
