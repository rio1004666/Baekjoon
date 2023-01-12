import sys
si = sys.stdin.readline

n, s = map(int, si().split())
arr = list(map(int, si().split()))
visited = [False] * (n)
ans = 0
def nCr(pos,accum):
    global s, ans
    if pos == n:
        if accum == s:
            ans += 1
        return
    nCr(pos + 1, accum + arr[pos])
    nCr(pos + 1, accum)

nCr(0,0)
# 전부 안골랐을 경우 0이 되므로 -1해줘야함
if s == 0:
    print(ans-1)
else:
    print(ans)