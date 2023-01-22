"""
bfs로 풀기
완전탐색이라고 해서 무작정 dfs 로 푸는것도 아니야...
그리고 방문했던 알파벳을 체크하는 용도로 무조건 배열만 있는것도 아니야...
set도 있어....
이미 지나갓던 길을 다시는 가지 않는다는 유망한 가능성을 배제함으로써 시간을 단축한다
"""
import sys
si = sys.stdin.readline
r,c = map(int, si().split())

board = [list(si().strip()) for _ in range(r)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
answer = 1
def in_range(nx,ny):
    return  0 <= nx < r and 0 <= ny < c

def bfs(sx,sy):
    global answer
    q = set([(sx,sy,board[sx][sy])])
    while q:
        cx,cy,dist = q.pop()
        for i in range(4):
            nx,ny = cx + dx[i], cy + dy[i]
            if not in_range(nx,ny):continue
            if board[nx][ny] in dist:continue
            q.add((nx,ny,dist + board[nx][ny]))
            answer = max(answer, len(dist)+1)




bfs(0,0)
print(answer)
