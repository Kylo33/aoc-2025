from collections import Counter, defaultdict, deque
import heapq

import sys
text = sys.stdin.read().strip()
grid = [list(line) for line in text.split('\n')]

deltas_4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
deltas_8 = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]


fresh, avail = text.split('\n\n')

fresh = fresh.split("\n")
avail = map(int, avail.split("\n"))

ans = 0
for a in avail:
    for f_range in fresh:
        start, end = map(int, f_range.split("-"))
        if start <= a <= end:
            ans += 1
            break

print(ans)
