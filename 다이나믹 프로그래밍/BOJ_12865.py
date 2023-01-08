# 평범한 배낭문제
# 물건들의 최댓값을 구하기
# 모든 물건을 가방에 넣어보며 경우를 다구해보며 최대의 가치를 구해보는 브루트포스 알고리즘 => 효율성탈락
# 다이나믹 프로그래밍
# 이 풀이에서는 2차원 전수 조사를 하기떄문에 오래걸린다;
MAX_VAL = 100000

n,k = tuple(map(int, input().split()))

dp = [[0] * (k+1) for _ in range(n+1)]
ans = 0
stuff = [(0,0)]
for _ in range(n):
    w,v = tuple(map(int , input().split()))
    stuff.append((w,v))
for i in range(1,n+1):
    for j in range(1,k+1):
        w,v = stuff[i][0], stuff[i][1]
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            # 이전가치보다 큰 가치를 만들 수 있다면 업데이트 한다
            dp[i][j] = max(dp[i-1][j] , dp[i-1][j-w] + v)
print(dp[n][k])

# 효율적인 구현
# 담을 수 있는 경우에만 담기
# 이 풀이는 1차원적으로 업데이트만 하기때문에 오래 걸리지 않는다
def solve():
    n, k = [int(x) for x in input().split()]
    table = [0] * (k + 1)
    for _ in range(n):
        w, v = [int(x) for x in input().split()]
        if w > k:
            continue
        # 조건으로 필터링하는 부분으로 시간 단축
        # 비교하는 연산시간도 오래걸린다
        for j in range(k, 0, -1):
            if j + w <= k and table[j] != 0:
                table[j + w] = max(table[j + w], table[j] + v)
        table[w] = max(table[w], v)
    print(max(table))


solve()











