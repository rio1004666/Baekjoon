"""
스도미도쿠
기본적인 스도쿠에다가
도미노 타일 추가
1부터 9까지 쌍이 모두 포함되어있고 중복되지 않음 (1,2)와 (2,1)은 중복으로 봄

기존에 1부터 9까지 숫자가 적힌것은 박힌것이므로 건드릴수없고
도미노 타일은 자리가 바뀔수 잇다...
6-1 로 인접한 도미노 타일이 있다면 1-6으로 바꾸고 문제를 풀 수 있다

    두 숫자를 묶은 블럭 단위로 일일이 넣어보는 완전탐색 및 구현

    처음부터 박힌 도미노 타일도 위치를 바꿀 수 있으므로
    여기서부터 dfs 탐색 해야함
    도미노 타일을 놓는 방법은
    4가지 방향으로 놓아본다??
    범위를 벗어나거나 숫자가 있는곳은 건너뛴다
    그리고 한숫자를 놓을때 인접한 4가지 방향중 한칸에 놓게 되므로
    놓았다는 표시를 해야 다음에 그 칸에서 탐색을 하지 않을것이다??

    그리고 한번 숫자를 놓을때마다 유망한지 판단한다
    근데 빈칸이 도미노타일이 최소 10개 처음부터 깔리면 20칸이 채워지고
    나머지 52칸을 채우는데...

    물론 두칸씩 채우기때문에 26칸을 채우는 꼴이 되지만 다 일일이 해봐야해?

    그것도 4칸 방향으로 탐색하면서?
    가능하겟다 어차피 4방향으로 돌면서

    안되는 건 패스하고 되는것만 놓아보고 그 다음 스텝 밟으니까

    근데 한가지 생각해줘야할건 기본의 도미노 타일의 위치 변경은
    생각하지 않나???

    또 (1,2),(1,3) 이렇게 쌍으로 넣어야하는데 흠.....

    이건 조합으로 뽑아야하고

    순서를 변경할 수 있으므로 순열이다 -> 2가지
    오른쪽 아래로 회전할 수 있음 -> 2가지
    2 x 2 = 4가지의 경우의 수로 정할 수 있다 한번 놓는데에
    굳이 방향 4가지 방향다 할 필요가 없다 이미 앞에서 채워졋기때문이다
    놓을 수 없는 경우는 생각하지 않는다

    또 2차원 격자에 구현하는 것이므로 구현에 해당한다

    아니면 다른 방법을 생각해보는건,...?

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
                if 0 <= px < MAX and 0 <= py < MAX and not board[px][py]:
                    if (row[x][i] == row[px][j] == col[y][i] == col[py][j] == s[x//3 * 3 + y//3][i] == s[px//3 * 3 + py//3][j] == 0):
                        row[x][i],row[px][j] = 1,1
                        col[y][i],col[py][j] = 1,1
                        visit[i][j] , visit[j][i] = 1,1
                        s[x//3 * 3 + y//3][i] , s[px//3 * 3 + py//3][j] = 1,1
                        board[x][y] , board[px][py] = i + 1 , j + 1
                        find = go(cnt+1,itr)
                        if find:
                            return True
                        row[x][i], row[px][j] = 0, 0
                        col[y][i], col[py][j] = 0, 0
                        visit[i][j], visit[j][i] = 0, 0
                        s[x // 3 * 3 + y // 3][i], s[px // 3 * 3 + py // 3][j] = 0, 0
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

    row = [[0]*MAX for _ in range(MAX)]
    col = [[0]*MAX for _ in range(MAX)]
    s = [[0]*MAX for _ in range(MAX)]
    visit = [[0]*MAX for _ in range(MAX)]
    emptys = []
    ecnt = 0


    # 도미노 타일들에 해당하는 값들을 격자에 넣어준다

    for _ in range(n):
        u,lu,v,lv = input().split()
        nu,nv = int(u) , int(v)
        ux,uy = ord(lu[0]) - ord('A') , int(lu[1]) - 1
        vx,vy = ord(lv[0]) - ord('A') , int(lv[1]) - 1
        row[ux][nu-1],row[vx][nv-1] = 1,1
        col[uy][nu-1],col[vy][nv-1] = 1,1
        visit[nu-1][nv-1],visit[nv-1][nu-1] = 1,1
        s[ux//3 * 3 + uy//3][nu-1] = 1
        s[vx//3 * 3 + vy//3][nv-1] = 1
        board[ux][uy] , board[vx][vy] = nu , nv

    # 숫자 한개가 박히는것들에 대해서 격자에 넣어준다 또 체크해준다

    for i,pos in enumerate(input().split()):
        pos_x , pos_y = ord(pos[0])-ord('A') , int(pos[1]) - 1
        row[pos_x][i] = 1
        col[pos_y][i] = 1
        s[pos_x//3 * 3 + pos_y//3][i] = 1
        board[pos_x][pos_y] = i + 1
    # 비어있는 칸에 대해서 탐색을 시작한다

    for i in range(MAX):
        for j in range(MAX):
            if not board[i][j]:
                emptys.append((i,j))
                ecnt += 1

    go(0,itr)

    itr += 1





