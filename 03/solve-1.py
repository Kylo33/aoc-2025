import sys
text = sys.stdin.read().strip()

banks = text.split("\n")

ans = 0
for bank in banks:
    max_val = 0

    for i, a in enumerate(bank):
        for j, b in enumerate(bank):
            if j <= i:
                continue
            max_val = max(max_val, int(f"{a}{b}"))

    ans += max_val

print(ans)
