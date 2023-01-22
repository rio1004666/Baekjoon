"""
알파벳
세로 R 가로 C칸 보드판
보드의 각 판에는 알파벳이 하나씩 적혀잇다
좌측 상단 1행1열에는 말이 놓여 있음
상하좌우로 인접한 네 칸 중 한 칸으로 이동 가능
새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온
모든 칸에 적인 알파벳이 아니여야 한다
즉, 같은 칸을 두 번 지날 수 없음
좌측 상단에서 시작해서 말이 최대한 몇 칸을 지날 수 있는지를 구하는 문제

입력 R,C 주어지고 범위는 1이상 20이하

말이 지날 수 있는 최대 칸 수

접근법
우선 R,C 가 20이하로 적다
완전탐색으로 모든 길 가는 방법을 탐색해보고 가장 멀리 간 거리로 업데이트한다
백트래킹
한번 지날 때마다 내가 지나왔던 알파벳중 현재 이 알파벳이 있었는지 체크하여 기록하는 변수 필요
dfs 진행시 오른쪽으로 가면서 왼쪽으로 갈 수도 있다

"""
import sys
si = sys.stdin.readline
R,C = map(int, si().split())
graph = [list(si())[:-1] for _ in range(R)]
visited = [[False]*C for _ in range(R)]
checkAlpha = [False] * 26
# for i in range(R):
#     print(*graph[i])
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def in_range(nx,ny):
    return 0 <= nx < R and 0 <= ny < C
ans = 1
def dfs(cx,cy,dist):
    global ans
    ans = max(ans, dist)
    # 다음 탐색할 4방향의칸을 정할려고 함
    for i in range(4):
        nx,ny = cx + dx[i], cy + dy[i]
        if not in_range(nx,ny) or visited[nx][ny]: continue
        nalpha = ord(graph[nx][ny]) - ord('A')
        if not checkAlpha[nalpha]:
            visited[nx][ny] = True
            checkAlpha[nalpha] = True
            dfs(nx,ny,dist+1)
            visited[nx][ny] = False
            checkAlpha[nalpha] = False

# 탐색이 끝나면 최대로 갈 수 있는 거리가 업데이트 되어 있음
# 0,0부터 시작해서 다음 갈 곳을 정함
# 초기 방문 설정 및 알파벳 체크 설정
calpha = ord(graph[0][0]) - ord('A')
checkAlpha[calpha] = True
visited[0][0] = True
dfs(0,0,1)
print(ans)




