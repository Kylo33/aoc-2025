with open('1') as f:
    text = f.read()

val = 50
ans = 0
for line in text.strip().split("\n"):
    move = int(line[1:])
    if line[0] == 'R':
        val = (val + move) % 100
    else:
        val = (val - move + 100) % 100

    if val == 0:
        ans += 1

print(ans)
