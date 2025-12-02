with open('1') as f:
    txt = f.read().strip()

ranges = txt.split(',')
ans = 0

for rng in ranges:
    first, second = map(int, rng.split('-'))
    for num in range(first, second + 1):
        snum = str(num)
        for num_parts in range(2, len(snum) + 1):
            if len(snum) % num_parts != 0:
                continue

            strs = set()
            for i in range(num_parts):
                strs.add(snum[i * len(snum) // num_parts:(i + 1) * len(snum) // num_parts])

            if len(strs) == 1:
                ans += num
                break


print(ans)

