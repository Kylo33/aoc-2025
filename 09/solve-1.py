from collections import Counter, defaultdict, deque
import heapq

import sys
text = sys.stdin.read().strip()
grid = [list(line) for line in text.split('\n')]
lines = text.split("\n")

deltas_4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
deltas_8 = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

points = list(map(lambda x: list(map(int, x.split(","))), lines))

ans = 0
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        x1, y1 = points[i]
        x2, y2 = points[j]
        area = (abs(x2-x1)+1) * (abs(y2-y1)+1)
        print(area, points[i], points[j])
        ans = max(ans, area)

print(ans)
