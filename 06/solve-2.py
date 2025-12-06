import re
from collections import Counter, defaultdict, deque
import heapq

import sys
text = sys.stdin.read().strip()
grid = [list(line) for line in text.split('\n')]

deltas_4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
deltas_8 = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

lines = text.split('\n')
lines = [line.replace('.', ' ') for line in lines] # edit the input to have the last space as a period, yes this is my solution.

num_sets = [[]]
rows = ["".join(x) for x in zip(*lines)]
for row in rows:
    s = re.sub(r"[ +*]*", "", row).strip()
    if s:
        num_sets[-1].append(int(s))
    else:
        num_sets.append([])


ans = 0
operations = list(lines[-1].replace(" ", ""))
for i, num_set in enumerate(num_sets):
    if operations[i] == '+':
        ans += sum(num_set)
    else:
        val = 1
        for num in num_set:
            val *= num
        ans += val

print(ans)
