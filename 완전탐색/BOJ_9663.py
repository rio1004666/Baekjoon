"""
n - QUEEN 문제

백트래킹 문제

퀸을 놓을 수 없다면 다시 돌아감
n제한 <= 15
모든 경우를 다세보는 완전탐색 방법
2차원격자
퀸을 놓을때마다 일직선상 대각선 다 체크 해보아야 한다

놓을 수 없다면 다시 돌아간다 이전상태로.......

탐색하기전에 이곳에 퀸을 놓을 수 있는지 판단하는 함수 필요

가로 세로 일직선상에서 판단하는것은

같은 행이냐 열이냐 판단하고

대각선은 흠....

한번 뎁스로 들어가서 탐색하게 되면 일직선방향 대각선방향 모두 체크하기....????

그래...굳이 2차원배열을 사용하지 않는거야
컬럼이 겹치지 않게끔 하는거야...
근데 일직선 대각선을 어떻게 피해서 퀸을 놓게해?

그치... 아이디어 생각해야함 행과 열을 이용해서 ...
행차이와 열차이가 같으면 놓을수 있다고 판단


"""

import sys

n = int(sys.stdin.readline().rstrip())

ans = 0
row = [0] * n


def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False

    return True


def n_queens(x):
    global ans
    if x == n:
        ans += 1

    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            if is_promising(x):
                n_queens(x + 1)


n_queens(0)
print(ans)





