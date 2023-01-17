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