"""
n-queen문제
2차원이 아닌 행과 열을 일차원의 인덱스와 값으로 표현하였다는 점이 특징
2차원으로 풀엇다면 시간초과일 뿐더러 코드가 난잡해짐
한뎁스씩 탐색해갈떄마다 놓을 수 있는지 판단하고 탐색할 수 잇음
즉 놓을수잇는지 판단하기 위해 일직선상과 대각선을 탐색해본 후 놓고
다시 이전상태로 백트래킹하여 다른곳에 놓을 수 있는지 판단함
"""
n = int(input())
board = [0]*15

def is_promising(pos):
    # 행 열을 대각선을 다 체크해본다
    for i in range(pos):
        if board[pos] == board[i] or ((pos-i) == abs(board[pos] - board[i])):
            return False
    return True

ans = 0

def dfs(pos):
    global ans
    if pos == n:
        ans += 1
        return
    for i in range(n):
        board[pos] = i # pos행 i열에 퀸을 놓아본다
        if is_promising(pos):
            dfs(pos+1)
dfs(0)
print(ans)