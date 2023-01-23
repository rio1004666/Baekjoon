"""
n+1일째 퇴사하는 백준이
그 전에 가능한 상담읊 최대한 많이 해서 최대 수익을 올리고 싶은데 그 최대 수익을 구하기

n <= 15이므로 완탐을 생각해볼 수 있다
1알부터 상담했을 때 그리고 상담안하고 2일부터 상담했을 때 이렇게
모든 경우를 다 따져 본다
근데 1일에 상담을 했다면 2일 3일은 상담할 수 없음

그렇게 하다가 남은 일수를 다 채우게 되면 최댓값을 구한다

한번씩 탐색뎁스가 들어가기전에 n+1보다 작냐고 물어봐야함
작으면 탐색하고 아니면 패스한다

"""

n = int(input())
consult = []
for _ in range(n):
    t,p = map(int, input().split())
    consult.append((t,p))

ans = 0
def dfs(pos,profit):
    global ans
    ans = max(ans, profit)
    for i in range(pos, n):
        if i + consult[i][0] <= n:
            dfs(i + consult[i][0], profit + consult[i][1])

for i in range(n):
    if i + consult[i][0] <= n:
        dfs(i + consult[i][0],consult[i][1])
print(ans)