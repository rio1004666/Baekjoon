import sys
from collections import deque
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
def bfs(ix1,iy1,ix2,iy2):
    global ans
    init = (ix1,iy1,ix2,iy2,0)
    q = deque([init])

    while q:
        cx1,cy1,cx2,cy2,cnt = q.popleft()
        if cnt >= 10:
            return
        else:
            cnt = cnt + 1  # 한칸 이동함
            for i in range(4):
                # 다음 상태를 방문함 즉 다음 노드를 방문함
                nx1,ny1 = cx1 + dx[i] , cy1 + dy[i]
                nx2,ny2 = cx2 + dx[i] , cy2 + dy[i]

                #찾는순간 더이상 탐색하지 않아도됨
                if (drop_check(nx1,ny1)) ^ (drop_check(nx2,ny2)):
                    ans = min(ans,cnt)
                    return
                elif (drop_check(nx1,ny1) & (drop_check(nx2,ny2))):
                    continue
                else:
                    if board[nx1][ny1] == '#':
                        nx1,ny1 = cx1,cy1
                    if board[nx2][ny2] == '#':
                        nx2,ny2 = cx2,cy2
                    q.append((nx1,ny1,nx2,ny2,cnt))


bfs(x[0],y[0],x[1],y[1])
if ans == sys.maxsize:
    print(-1)
else:
    print(ans)