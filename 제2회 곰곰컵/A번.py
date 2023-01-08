import sys
si = sys.stdin.readline
ans = 0
n = int(si())
for _ in range(n):
    deadline = si()
    chars,days = deadline.split('-')
    intdays = int(days)
    if intdays <= 90:
        ans += 1
print(ans)