import sys
text = sys.stdin.read().strip()

banks = text.split("\n")

ans = 0
for bank in banks:
    max_val = 0

    dp = [[0] * 13 for _ in range(len(bank))]

    # dp[i][j] = biggest number in string from i..N using j digits
    for i in range(len(dp)):
        dp[i][1] = int(bank[i])

    for i in range(len(dp) - 2, -1, -1):
        for j in range(1, len(dp[0])):
            dp[i][j] = max(dp[i+1][j], int(f"{bank[i]}{dp[i+1][j-1]}") if j - 1 >= 1 else int(bank[i]))

    ans += dp[0][12]

print(ans)
