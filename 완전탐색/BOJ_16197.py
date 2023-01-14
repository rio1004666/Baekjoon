"""
NxM크기의 보드와 4개의 버튼으로 이루어진 게임이 있다.
왼쪽 오른쪽 위 아래 4가지 있다
버튼을 누르면 두 동전이 버튼에 쓰여 있는 방향으로 동시에 이동한다
동전이 이동하려는 칸이 벽이면 동전은 이동x
동전이 이동하려는 방향에 칸이 없으면 떨어짐
그외 경우에 이동하려는 방향으로 한 칸 이동
이동하려는 칸에 동전이 있는 경우에도 한 칸 이동
두 동전중 하나만 보드에서 떨어뜨리기 위해 버튼을 최소 몇번눌러야하는지
"""
"""
우선 1번 버튼을 눌러본다 각 방향에 대해서 
그리고 1번 버튼을 누른 각 방향에 대해 또 4가지 방향으로 버튼을 누른다 
2번누르고 떨어지는지 확인......
이렇게 동전이 하나만 떨어지는 순간을 찾은 후 
더이상탐색하지 않고 돌아온다 

버튼을 누르면서 동전의 상태가 노드가 됨 
동전의 상태를 탐색하면서 횟수를 체크해감 
bfs 사용해도 됨 
그래프 문제가 됨



"""
import sys
si = sys.stdin.readline
n, m = map(int, si().split())
board = [list(si().rstrip()) for _ in range(n)]
x,y = [0,0] , [0,0]
k = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'o':
            x[k],y[k] = i,j
            k += 1
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = sys.maxsize
def drop_check(temp_r, temp_c) :
    if( (temp_r<0)|(temp_r>=n)|(temp_c<0)|(temp_c>=m) ) :
        return True
    return False

def dfs(cx1,cy1,cx2,cy2,cnt):
    global ans
    # 10번이상은 더이상 탐색하지 않음
    if ((cnt >= 10)):
        return
    # 동쪽으로 공1,2가 이동함
    else:
        cnt = cnt + 1
        for i in range(4):
            nx1,ny1 = cx1 + dx[i] , cy1 + dy[i]
            nx2,ny2 = cx2 + dx[i] , cy2 + dy[i]
            # 공하나만 떨어진다면 즉각 리턴한다
            if (drop_check(nx1,ny1) ^ drop_check(nx2,ny2)):
                ans = min(ans,cnt)
                return
            # 공 두개 다 떨어진다면 다른 방향으로 탐색한다
            elif (drop_check(nx1,ny1) & drop_check(nx2,ny2)):
                continue
            else:
                if board[nx1][ny1] == '#':
                    nx1,ny1 = cx1,cy1
                if board[nx2][ny2] == '#':
                    nx2,ny2 = cx2,cy2
                dfs(nx1, ny1, nx2, ny2, cnt )

dfs(x[0],y[0],x[1],y[1],0)
if ans == sys.maxsize:
    print(-1)
else:
    print(ans)



