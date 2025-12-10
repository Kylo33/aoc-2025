from collections import Counter, defaultdict, deque
import heapq
from z3 import *

import sys
text = sys.stdin.read().strip()
grid = [list(line) for line in text.split('\n')]
lines = text.split("\n")

deltas_4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
deltas_8 = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

ans = 0
for line in lines:
    parts = line.split(" ")
    target = list(map(int, parts[-1][1:-1].split(',')))
    button_parts = parts[1:-1]
    buttons = []
    for i,button_part in enumerate(button_parts):
        buttons.append((Int(f"b{i}"), list(map(int, button_part[1:-1].split(",")))))

    s = Optimize()
    contributors = [[] for _ in range(len(target))]
    for button_var, button in buttons:
        for val in button:
            contributors[val].append(button_var)
        s.add(button_var >= 0)

    for elem, cont_list in enumerate(contributors):
        s.add(sum(cont_list) == target[elem])

    s.minimize(sum(button_var for button_var, _ in buttons))
    s.check()
    m = s.model()
    ans += sum(m[button_var].as_long() for button_var, _ in buttons)

print(ans)
