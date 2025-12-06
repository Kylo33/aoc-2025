import re
from collections import Counter, defaultdict, deque
import heapq

import sys
text = sys.stdin.read().strip()
grid = [list(line) for line in text.split('\n')]

deltas_4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
deltas_8 = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

lines = text.split('\n')

grid_parsed = []

for i, line in enumerate(lines):
    m = re.sub(r" +", " ", line)
    if i < len(lines) - 1:
        m = list(map(int, m.split()))
    else:
        m = list(m.split())

    grid_parsed.append(m)

ans = 0
num_sets = [list(x) for x in zip(*grid_parsed[:-1])]
for i, num_set in enumerate(num_sets):
    operation = grid_parsed[-1][i]
    if operation == '+':
        ans += sum(num_set)
    else:
        val = 1
        for num in num_set:
            val *= num
        ans += val

print(ans)    
