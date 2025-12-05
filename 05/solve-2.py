from collections import Counter, defaultdict, deque
import heapq

import sys
text = sys.stdin.read().strip()
grid = [list(line) for line in text.split('\n')]

deltas_4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
deltas_8 = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

fresh_ranges = text.split('\n\n')[0]
fresh_ranges = [list(map(int, rng.split("-"))) for rng in fresh_ranges.split('\n')]

heapq.heapify(fresh_ranges)

ans = 0

while fresh_ranges:
    start, end = heapq.heappop(fresh_ranges)
    if fresh_ranges and fresh_ranges[0][0] <= end:
        other_start, other_end = heapq.heappop(fresh_ranges)
        end = max(end, other_end)
        heapq.heappush(fresh_ranges, [start, end])
    else:
        ans += end - start + 1

print(ans)

