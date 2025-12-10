from collections import Counter, defaultdict, deque
import heapq

import sys
text = sys.stdin.read().strip()
grid = [list(line) for line in text.split('\n')]
lines = text.split("\n")

deltas_4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
deltas_8 = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

ans = 0
for line in lines:
    parts = line.split(" ")
    target = int(parts[0][1:-1].replace(".","0").replace("#","1"),2)

    options = []
    for button_part in parts[1:-1]:
        button_part = button_part[1:-1]
        nums = list(map(int, button_part.split(",")))
        v=0
        for num in nums:
            v |= 1 << (len(parts[0]) - 3 - num)
        options.append(v)
    
    q = deque([(0, 0)])
    seen = set()
    while q:
        state, presses = q.popleft()
        if state == target:
            break
        if state in seen:
            continue
        seen.add(state)
        for option in options:
            q.append((state ^ option, presses + 1))

    ans += presses

print(ans)
