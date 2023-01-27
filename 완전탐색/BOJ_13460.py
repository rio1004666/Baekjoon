"""
구슬탈출2....
상하좌우 움직여보며 빨간공만 탈출했을때 움직인 최소 횟수
상하좌우 움직여보면서 빨간구슬만 빠졋는지 확인하면 되는 완전탐색으로 접근 시도
파란 구슬은 빠지면 안됨
bfs로 구할 수 있음
탐색 대상은 상하좌우로 움직였을때 보드판의 상태가 노드가 되고
상하좌우로 움직이는 행위가 간선이 된다.....
그런데 못빠져 나올수도 잇는데
멈추는 조건은 ?
이미 방문한 노드는 빨간색구슬과 파란색구슬의 좌료가 되나
그러네 즉 한번 간선을 타고 즉 상하좌우로 이동 햇을 경우 빨간구슬과 파란구슬의 위치를 기억해서 방문했다고 표시해야
다음 그 상태로 가더라도 이미 방문한것을 다시 그 상태로 안가게 하면
언젠가 끝난다

자료구조를 어떻게 만들어야 할까?
일단 R이랑 B랑 같은 행이나 열에 있다면 즉
상하로 움직일때는 같은 열에 있고
좌우로 움직일때는 같은 행에 있다면
더 앞쪽에 있는 구슬이 먼저 움직여야 한다
그리고 빨간구슬이랑 파란구슬이랑 이 두개의 위치를 방문했다는 표시로
4차원 배열을 하나 선언해주어야 함

그리고 bfs 탐색방식으로
첫 위치를 rx,ry,bx,by 부터 시작한다
그리고 4방향으로 움직이는 간선을 타고
이동하는 함수를 만들어서 수행한다
상하좌우로 움직일때마다 +1 카운팅을 해줘서
최소 횟수를 구한다
즉 최단거리를 구한다
최단거리는 bfs 알고리즘 구하기
이 문제에서 노드는 빨간구슬과 파란구슬의 위치이고
간선은 이동하는 행위이다 4방향으로
"""

import sys
from collections import deque
from collections import defaultdict
si = sys.stdin.readline
n,m = tuple(map(int, si().split()))
board = [list(si().rstrip()) for _ in range(n)]
dxs = [0,1,0,-1]
dys = [1,0,-1,0]
rx,ry,bx,by = 0,0,0,0
visited = defaultdict(lambda : 0)# 빨간구슬과 파란구슬의 위치를 체크할 기억장치

# 빨간구스로가 파란구승릉 움직인다
def lean_board(rcx,rcy,bcx,bcy,move_dir):
    # 출발할 위치를 지정해준다 그리고 최종적으로 이동한 위치에서 다시 출발할 위치를 지정해주는 방식으로 반복한다
    board[rcx][rcy] = 'R'
    board[bcx][bcy] = 'B'
    # 그리고 탐색을 한번씩 시도하였을 때 다음 위치륽 구하고 다시 초기화해야한다
    rnx,rny,bnx,bny = rcx,rcy,bcx,bcy
    if move_dir == 0:
        # 파란공이 빨간공보다 오른쪽에 있다면
        if rny < bny:
            while board[bnx + dxs[move_dir]][bny + dys[move_dir]] == '.':
                board[bnx][bny] = '.'
                bnx += dxs[move_dir]
                bny += dys[move_dir]
                board[bnx][bny] = 'B'
            if board[bnx + dxs[move_dir]][bny + dys[move_dir]] == 'O':
                board[bnx][bny] = '.'
                bnx, bny = bnx + dxs[move_dir], bny + dys[move_dir]
            # 파란공부터 움직인다
            while board[rnx+dxs[move_dir]][rny+dys[move_dir]] == '.':
                board[rnx][rny] = '.'
                rnx += dxs[move_dir]
                rny += dys[move_dir]
                board[rnx][rny] = 'R'
            if board[rnx+dxs[move_dir]][rny+dys[move_dir]] == 'O':
                board[rnx][rny] = '.'
                rnx,rny = rnx + dxs[move_dir] , rny + dys[move_dir]

        else:

            while board[rnx+dxs[move_dir]][rny+dys[move_dir]] == '.':
                board[rnx][rny] = '.'
                rnx += dxs[move_dir]
                rny += dys[move_dir]
                board[rnx][rny] = 'R'
            if board[rnx+dxs[move_dir]][rny+dys[move_dir]] == 'O':
                board[rnx][rny] = '.'
                rnx,rny = rnx + dxs[move_dir] , rny + dys[move_dir]
            while board[bnx+dxs[move_dir]][bny+dys[move_dir]] == '.':
                board[bnx][bny] = '.'
                bnx += dxs[move_dir]
                bny += dys[move_dir]
                board[bnx][bny] = 'B'
            if board[bnx+dxs[move_dir]][bny+dys[move_dir]] == 'O':
                board[bnx][bny] = '.'
                bnx,bny = bnx + dxs[move_dir] , bny + dys[move_dir]
    if move_dir == 1:
        # 파란공이 빨간공보다 오른쪽에 있다면
        if rnx < bnx:
            while board[bnx + dxs[move_dir]][bny + dys[move_dir]] == '.':
                board[bnx][bny] = '.'
                bnx += dxs[move_dir]
                bny += dys[move_dir]
                board[bnx][bny] = 'B'
            if board[bnx + dxs[move_dir]][bny + dys[move_dir]] == 'O':
                board[bnx][bny] = '.'
                bnx, bny = bnx + dxs[move_dir], bny + dys[move_dir]
            # 파란공부터 움직인다
            while board[rnx+dxs[move_dir]][rny+dys[move_dir]] == '.':
                board[rnx][rny] = '.'
                rnx += dxs[move_dir]
                rny += dys[move_dir]
                board[rnx][rny] = 'R'
            if board[rnx+dxs[move_dir]][rny+dys[move_dir]] == 'O':
                board[rnx][rny] = '.'
                rnx,rny = rnx + dxs[move_dir] , rny + dys[move_dir]
        else:
            while board[rnx+dxs[move_dir]][rny+dys[move_dir]] == '.':
                board[rnx][rny] = '.'
                rnx += dxs[move_dir]
                rny += dys[move_dir]
                board[rnx][rny] = 'R'
            if board[rnx+dxs[move_dir]][rny+dys[move_dir]] == 'O':
                board[rnx][rny] = '.'
                rnx,rny = rnx + dxs[move_dir] , rny + dys[move_dir]
            while board[bnx+dxs[move_dir]][bny+dys[move_dir]] == '.':
                board[bnx][bny] = '.'
                bnx += dxs[move_dir]
                bny += dys[move_dir]
                board[bnx][bny] = 'B'
            if board[bnx+dxs[move_dir]][bny+dys[move_dir]] == 'O':
                board[bnx][bny] = '.'
                bnx,bny = bnx + dxs[move_dir] , bny + dys[move_dir]

    if move_dir == 2:
        if rny < bny:
            while board[rnx+dxs[move_dir]][rny+dys[move_dir]] == '.':
                board[rnx][rny] = '.'
                rnx += dxs[move_dir]
                rny += dys[move_dir]
                board[rnx][rny] = 'R'
            if board[rnx+dxs[move_dir]][rny+dys[move_dir]] == 'O':
                board[rnx][rny] = '.'
                rnx,rny = rnx + dxs[move_dir] , rny + dys[move_dir]
            while board[bnx + dxs[move_dir]][bny + dys[move_dir]] == '.':
                board[bnx][bny] = '.'
                bnx += dxs[move_dir]
                bny += dys[move_dir]
                board[bnx][bny] = 'B'
            if board[bnx + dxs[move_dir]][bny + dys[move_dir]] == 'O':
                board[bnx][bny] = '.'
                bnx, bny = bnx + dxs[move_dir], bny + dys[move_dir]
        else:
            while board[bnx+dxs[move_dir]][bny+dys[move_dir]] == '.':
                board[bnx][bny] = '.'
                bnx += dxs[move_dir]
                bny += dys[move_dir]
                board[bnx][bny] = 'B'
            if board[bnx+dxs[move_dir]][bny+dys[move_dir]] == 'O':
                board[bnx][bny] = '.'
                bnx,bny = bnx + dxs[move_dir] , bny + dys[move_dir]
            while board[rnx+dxs[move_dir]][rny+dys[move_dir]] == '.':
                board[rnx][rny] = '.'
                rnx += dxs[move_dir]
                rny += dys[move_dir]
                board[rnx][rny] = 'R'
            if board[rnx+dxs[move_dir]][rny+dys[move_dir]] == 'O':
                board[rnx][rny] = '.'
                rnx,rny = rnx + dxs[move_dir] , rny + dys[move_dir]
    if move_dir == 3:
        # 파란공이 빨간공보다 오른쪽에 있다면
        if rnx < bnx:
            # 파란공부터 움직인다
            while board[rnx+dxs[move_dir]][rny+dys[move_dir]] == '.':
                board[rnx][rny] = '.'
                rnx += dxs[move_dir]
                rny += dys[move_dir]
                board[rnx][rny] = 'R'
            if board[rnx+dxs[move_dir]][rny+dys[move_dir]] == 'O':
                board[rnx][rny] = '.'
                rnx,rny = rnx + dxs[move_dir] , rny + dys[move_dir]
            while board[bnx + dxs[move_dir]][bny + dys[move_dir]] == '.':
                board[bnx][bny] = '.'
                bnx += dxs[move_dir]
                bny += dys[move_dir]
                board[bnx][bny] = 'B'
            if board[bnx + dxs[move_dir]][bny + dys[move_dir]] == 'O':
                board[bnx][bny] = '.'
                bnx, bny = bnx + dxs[move_dir], bny + dys[move_dir]
        else:
            while board[bnx+dxs[move_dir]][bny+dys[move_dir]] == '.':
                board[bnx][bny] = '.'
                bnx += dxs[move_dir]
                bny += dys[move_dir]
                board[bnx][bny] = 'B'
            if board[bnx+dxs[move_dir]][bny+dys[move_dir]] == 'O':
                board[bnx][bny] = '.'
                bnx,bny = bnx + dxs[move_dir] , bny + dys[move_dir]
            while board[rnx+dxs[move_dir]][rny+dys[move_dir]] == '.':
                board[rnx][rny] = '.'
                rnx += dxs[move_dir]
                rny += dys[move_dir]
                board[rnx][rny] = 'R'
            if board[rnx+dxs[move_dir]][rny+dys[move_dir]] == 'O':
                board[rnx][rny] = '.'
                rnx,rny = rnx + dxs[move_dir] , rny + dys[move_dir]
    board[rcx][rcy] , board[bcx][bcy] = '.','.'
    if board[rnx][rny] == 'R':
        board[rnx][rny] = '.'
    if board[bnx][bny] == 'B':
        board[bnx][bny] = '.'
    return rnx,rny,bnx,bny

for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx,ry = i,j
        elif board[i][j] == 'B':
            bx,by = i,j

visited[(rx,ry,bx,by)] = 1 # 첫노드를 방문했음을 표시함
q = deque([(rx,ry,bx,by,0)]) # 탐색하기 위해 첫노드를 삽입함
ans = -1 # 탐색 종료 후 답을 찾지 못했을 경우  -1을 출력한다
while q:
    rcx,rcy,bcx,bcy,cnt = q.popleft()
    # 빨간구슬의 위치가 O이고 파란구슬위이치가 O가 아니라면 정답이다 빠져나온다 바로
    #print(rcx,rcy,bcx,bcy)
    if cnt > 10:
        break
    if board[rcx][rcy] == 'O' and board[bcx][bcy] != 'O':
        ans = cnt
        break
    for d in range(4):
        # 한위치에서 4방향으로 탐색한다
        rnx,rny,bnx,bny = lean_board(rcx,rcy,bcx,bcy,d)  # 해당 방향으로 보드판을 기울인다
        if board[rnx][rny] == 'O' and board[bnx][bny] == 'O': continue # 두개의 구슬이 모두 빠지는 경우는 더이상 탐색하지 않음
        if board[rnx][rny] != 'O' and board[bnx][bny] == 'O': continue # 파란구슬이 빠지고 빨간구슬이 빠지는 경우는 더이상 탐색하지 않음
        if visited[(rnx,rny,bnx,bny)]:continue # 이미 방문한 노드라면 패스한다
        visited[(rnx,rny,bnx,bny)] = 1
        q.append((rnx,rny,bnx,bny,cnt+1))
    # 각각 4방향으로 이동 후 원래 자리는 빈칸으로 비워준다

print(ans)




