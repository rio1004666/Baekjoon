"""
스도미노쿠 다른 관점으로 풀이

3x3격자를 전체에서 봤을때 9x9관점에서 봤을때 9부분으로 나누어서 볼 수 잇다
즉 9x9에서 첫 3x3격자의 첫부분을 0,0으로 보고 두번재 3x3격자에서 0,1로 본다 왜냐면 3으로 나눈값들이 공통으로 0,1을 가리키기 때문이다
예를들어 첫 3x3격자안의 좌표들은 3으로 전부 나누었을 경우 (0,0)으로 나타내고 두번째 3x3격자는 3으로 나누었을 때 (0,1)로 나타낼 수 있다

"""

def go(cnt,itr):
    find = False
    if cnt == ecnt:
        print('Puzzle',itr)
        for i in range(MAX):
            for j in range(MAX):
                print(board[i][j], end='')
            print()
        return True

    x,y = emptys[cnt]

    if board[x][y]:
        find = go(cnt+1,itr)
        return find

    for i in range(MAX):
        for j in range(MAX):
            if i == j or visit[i][j]:continue
            for d in dr:
                px ,py = x + d[0] , y + d[1]
                # 범위 안에 속해야하고 빈칸이어야함
                if 0 <= px < MAX and 0 <= py < MAX and not board[px][py]:
                    # 행,열,3x3격자안을 다 체크해봐야함
                    if (row[x][i] == row[px][j] == col[y][i] == col[py][j] == s[x//3][y//3][i] == s[px//3][py//3][j] == 0):
                        # 그제서야 숫자를 놓을 수 있음
                        row[x][i],row[px][j] = 1,1
                        col[y][i],col[py][j] = 1,1
                        visit[i][j] , visit[j][i] = 1,1
                        s[x//3][y//3][i] , s[px//3][py//3][j] = 1,1
                        board[x][y] , board[px][py] = i + 1 , j + 1
                        find = go(cnt+1,itr)
                        if find:
                            return True
                        # 백트래킹하는 부분
                        row[x][i], row[px][j] = 0, 0
                        col[y][i], col[py][j] = 0, 0
                        visit[i][j], visit[j][i] = 0, 0
                        s[x // 3][y // 3][i], s[px // 3][py // 3][j] = 0, 0
                        board[x][y], board[px][py] = 0, 0
    return find


itr = 1
MAX = 9
while True:

    dr = [(0, 1), (1, 0)]
    n = int(input())
    if n == 0:
        break
    board = [[0]*MAX for _ in range(MAX)]
    # 각 행 , 열 , 3x3 격자안에 넣을 숫자가 유일한지 판단하기 - 복잡도 O(1)로 접근하기 위한 자료구조 생성
    row = [[0]*MAX for _ in range(MAX)] #
    col = [[0]*MAX for _ in range(MAX)]
    s = [[[0]*MAX for _ in range(3)] for _ in range(3)]
    visit = [[0]*MAX for _ in range(MAX)]
    emptys = []
    ecnt = 0


    # 도미노 타일들에 해당하는 값들을 격자에 넣어준다

    for _ in range(n):
        u,lu,v,lv = input().split()
        nu,nv = int(u) , int(v)
        ux,uy = ord(lu[0]) - ord('A') , int(lu[1]) - 1
        vx,vy = ord(lv[0]) - ord('A') , int(lv[1]) - 1
        row[ux][nu-1],row[vx][nv-1] = 1,1 # 현재 ux,vx 행에 nu-1,nv-1이 이미 존재합니다 라고 체크해주기 위한 자료구조
        col[uy][nu-1],col[vy][nv-1] = 1,1 # 현재 uy,vy 열에 nu-1,nv-1이 이미 존재합니다 라고 체크해주기 위한 자료구조
        visit[nu-1][nv-1],visit[nv-1][nu-1] = 1,1
        # 3x3 격자에서 숫자가 있는지 체크하기 위해서 좌표를 번호로 바꾸는 트릭을 썻다 즉 첫번째 3x3격자범위내에있는 수들을 그룹핑하여 0번으로 귀속시켰다
        # 두번재 3x3격자에 있는 숫자들을 모아서 그룹핑하여 1번으로 귀속시켰다
        s[ux//3][uy//3][nu-1] = 1 # 현재 3x3 격자 같은 공간안에서 ux,uy에 위치한 곳에 nu-1이 존재합니다라고 체크해주기 위한 자료구조
        s[vx//3][vy//3][nv-1] = 1 # 현재 3x3 격자 같은 공간안에서 vx,vy에 위치한 곳에 nv-1이 존재합니다라고 체크해주기 위한 자료구조
        board[ux][uy] , board[vx][vy] = nu , nv

    # 숫자 한개가 박히는것들에 대해서 격자에 넣어준다 또 체크해준다

    for i,pos in enumerate(input().split()):
        pos_x , pos_y = ord(pos[0])-ord('A') , int(pos[1]) - 1
        row[pos_x][i] = 1
        col[pos_y][i] = 1
        s[pos_x//3][pos_y//3][i] = 1
        board[pos_x][pos_y] = i + 1
    # 비어있는 칸에 대해서 탐색을 시작한다

    for i in range(MAX):
        for j in range(MAX):
            if not board[i][j]:
                emptys.append((i,j))
                ecnt += 1

    go(0,itr)

    itr += 1





