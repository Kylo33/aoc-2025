with open('1') as f:
    txt = f.read().strip()

ranges = txt.split(',')
ans = 0

for rng in ranges:
    first, second = map(int, rng.split('-'))
    for num in range(first, second + 1):
        snum = str(num)
        if len(snum) % 2 == 0 and snum[:len(snum)//2] == snum[len(snum)//2:]:
            ans += num


print(ans)

