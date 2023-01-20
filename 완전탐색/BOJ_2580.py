"""
스도쿠 문재
모든 가로세로줄에 1부터 9까지 하나씩 들어가 있어야 한다
3x3 정사각형 안에 1부터 9까지 들어가 잇어야한다
흠 완탐으로 가능?
어떤 방법으로 풀어야하는걸까?

모든 칸에 빈칸이라면?

1부터 9까지 모두 있어야한다

3x3정사각형씩 끊어서 답을 구하면?
어차피 3x3정사각형 안에도 1부터 9까지 하나씩 등장해야함
3x3안에서 우선 필요한 수를 뽑는다
1번 정사각형에서 1,4,9 가 필요하다
그럼 1,4,9를 번갈아 돌려가며 넣어본다 순열처럼 순서만 바꿔서
그리고 넣어보고 가로세로줄 체크하면서 그 수가 있는지 확인한다

근데 문제는 다른 정사각형에는 영향이 안가나?

먼가 다른방법이 잇긴할건데....nqueenc처럼
근데 nqueen도 2차원이엇고 15x15엿자나?
이것도 그럼 유망한지 판단하는 근거를 가지고
일차원배열 형식으로 풀면 가능할듯?>
하나씩 놓아보자 라는거지
근데 nqueen은 행이 계속 달라야햇고 유망한지 판단하는것과
범위가 사실 좁앗어;;
왜냐면 놓을 수 있는 자리가 계속 많이 없어지기 때문이야..
그런데 이 문제는 전부 놓을 수 있는 부분이야

무조건 놓을 수 있는 경우로 주어지고 답이 여러개라면
위에서 하는 방식이 상식적일거같은데?>
1번 정사각형 안에 숫자 1을 놓을 수 있는 방법은 여러가지겠지만

"""
"""

0인칸만 골라서 확인하면된다 전부확인할 필요없이 
그 좌표들만 모아서 1부터 9까지 각 칸에 전부 넣어보고 확인해본다 
모든 빈칸에 넣어보고 스도쿠가 완성되는 순간 출력한다 

"""
board = []
for i in range(9):
    board.append(list(map(int, input().split())))
blanks = []

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blanks.append((i,j))
size = len(blanks)

# 같은 행에 자기 자신 숫자가 있는지 체크한다
def checkRow(cx,target):
    for i in  range(9):
        if target == board[cx][i]:
            return False
    return True
# 같은 열에 자기 자신 숫자가 있는지 체크한다
def checkCol(cy, target):
    for i in range(9):
        if target == board[i][cy]:
            return False
    return True
# 3x3에 자기 자신 숫자가 있는지 체크한다
def checkRect(cx,cy,target):
    # 0~2 / 3~5 / 6~8
    # 시작위치를 구하는것은 현재 위치에서 3을 나누고 3을 곱함
    nx = cx // 3 * 3 # 시작위치 x를 셋팅하기
    ny = cy // 3 * 3 # 시작위치 y를 세팅하기
    # 3x3 정각형모양의 격자를 탐색한다
    for i in range(3):
        for j in range(3):
            if target == board[nx + i][ny + j]:
                return False
    return True

def dfs(pos):
    if pos == len(blanks):
        for k in range(9):
            print(*board[k])
        exit(0) # 완전히 종료하기
    for target in range(1,10):
        cx = blanks[pos][0]
        cy = blanks[pos][1]

        if checkRow(cx,target) and checkCol(cy,target) and checkRect(cx,cy,target):
            board[cx][cy] = target # 스도쿠에 숫자를 넣어본다
            dfs(pos+1)
            board[cx][cy] = 0 # 다시 원래대로 되돌린다

dfs(0)
