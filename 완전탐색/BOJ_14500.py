"""
2차원 격자 -> 칸 : 정점 상하좌우 이동 : 간선 으로 표현
칸을 하나씩 방문 -> 일정한 패턴으로
dfs 탐색 시작
특징: 4칸으로 모두 이동하는것
그런데 문제는 ㅗ ㅓ ㅏ ㅜ 모양은 별개로 탐색해야한다
탐색방향이 나눠진다 즉 두번째 칸을 탐색 후 양옆으로 달라지기때문에 그 칸에서 다시 탐색하게 된다
더이상 칸을 이동하지 않고
하지만 여기서 그 칸에서 양옆으로 갈라지는 경우를 제외하곤 나머지는
계속 그 다음 새로운 칸을 깊이있게 탐색하므로 같이 진행해줘야한다
즉 두번째 칸에서 다음 세번째 칸을 탐색하는 경우 두가지의 탐색방향을 선택해야한다
시간복잡도는 500x500 모든 칸에 대하여 dfs 탐색을 하는데 4칸만 탐색하므로
4가지 방향으로 각각에 대해 4번움직이므로 4^4= = 64이고
25000 x 64 이므로 160만정도이다 거기다 ㅗ ㅏ ㅓ ㅜ 모양까지 포함하므로 더될것이다
완전탐색 가능하다

"""
import sys

n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

ans = -sys.maxsize


def in_range(nx,ny):
    return 0 <= nx < n and 0 <= ny < m

def dfs(pos,cx,cy,accum):
    global ans
    # 완전탐색의 가지치기가 핵심이다
    # 앞르고 가야 할 칸이 3-pos칸인데 그 칸들을 최댓값으로 곱하여서
    # 현재칸의 값에서 더해도 정답보다 작다면 더이상 탐색하지 않을것이다 라고 미래를 예측한다

    if ans >= accum + max_val * (3 - pos):
        return
    if pos == 3:
        ans = max(ans,accum)
        return
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if not in_range(nx,ny) : continue
        if visited[nx][ny] : continue
        if pos == 1:
            visited[nx][ny] = True # 다음칸에는 안가겠다는 표시를 함
            dfs(pos+1,cx,cy,accum + board[nx][ny])
            visited[nx][ny] = False
        visited[nx][ny] = True
        dfs(pos+1,nx,ny,accum + board[nx][ny])
        visited[nx][ny] = False


dx = [0,1,0,-1]
dy = [1,0,-1,0]
max_val = max(map(max, board)) # 2차원 리스트의 최댓값 구하기
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(0,i,j,board[i][j])
        visited[i][j] = False
print(ans)