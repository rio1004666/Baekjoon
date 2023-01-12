import sys
si = sys.stdin.readline

flag = True


def nCr(pos,a,original,n,r):
    if pos == n:
        if len(a) == r:
            for num in a:
                print(num , end= ' ')
            print()
        return
    a.append(original[pos])
    nCr(pos+1,a,original,n,r)
    a.pop()
    nCr(pos+1,a,original,n,r)


while flag:
    arr = list(map(int,input().split()))
    if len(arr) == 1 and arr[0] == 0:
        break
    else:
        new_arr = arr[1:]
        nCr(0,[],new_arr,arr[0],6)
        print()
"""
1.조합 라이브러리 이용
"""
import itertools
while True:
    array = list(map(int, input().split()))
    k = array[0]
    S = array[1:]
    for i in itertools.combinations(S,6):
        print(*i)
    if k == 0:
        exit()
    print()
"""
2. 재귀 이용 
"""

def recur(depth,idx):
    if depth == 6:
        print(*out)
        return
    for i in range(idx,k):
        out.append(S[i])
        recur(depth+1,i+1)
        out.pop()

while True:
    array = list(map(int, input().split()))
    k = array[0]
    S = array[1:]
    out = []
    dfs(0,0)
    if k == 0:
        exit()
    print()
