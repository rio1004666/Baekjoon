

import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
answer = []

def dfs(value, index):
    if index == n:
        return 
    value += arr[index] # 한번이라도 탐색하게 되면
    answer.append(value) # 정답리스트에 추가한다
    dfs(value, index+1)
    value -= arr[index]
    dfs(value, index+1)

dfs(0,0)
a = set(answer)
for num in range(1, 2000000):
    if num not in a:
        print(num)
        break