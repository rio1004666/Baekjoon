"""
완전탐색 다른 풀이
"""

def revenue_making(idx,rev):
    global max_rev
    # 끝에 도착하는 순간
    if idx == n:
        # 업데이트함
        if max_rev < rev:
            max_rev = rev
        return
    # 현재날짜를 상담일로 정하지 않거나
    revenue_making(idx+1,rev)
    # 현재날짜를 상담일로 정함
    if idx + table[idx][0] <= n:
        revenue_making(idx + table[idx][0], rev+table[idx][1])
n = int(input())
table = []
for i in  range(n):
    t,p = map(int,  input().split())
    table.append((t,p))
max_rev = 0
revenue_making(0,0)