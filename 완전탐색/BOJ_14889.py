"""
20명중에 10명을 중복없이 고르면 된다
고른사람번호를 체크해두고 체크하지 않은것끼리 합하고 체크한것끼리 한한후 차이를 구해 최솟값을 업데이트 한다
완전탐색으로 일일이 골라보고 최솟값업데이트 때리는것이 가능한가??
"""
import sys
si = sys.stdin.readline
n = int(si())
members = [[0 for _ in range(n+1)]]
for _ in range(n):
    members.append([0]+list(map(int, si().split())))

selected = n // 2

nums = [num for num in range(1,n+1)]
answer_list = []
visited = [False] * (n+1)
min_val  = sys.maxsize
def get_sum(team):
    sum = 0
    for i in range(len(team)):
        for j in range(i+1,len(team)):
            m1, m2 = members[team[i]][team[j]], members[team[j]][team[i]]
            sum += (m1+m2)
    return sum
def nCr(pos, team1, r):
    global min_val
    if pos == len(nums):
        if len(team1) == r:
            team2 = []
            for i in range(1,n+1):
                if not visited[i]:
                    team2.append(i)
            sum1 = get_sum(team1)
            sum2 = get_sum(team2)
            min_val = min(min_val,abs(sum1-sum2))
        return
    team1.append(nums[pos])
    visited[nums[pos]] = True
    nCr(pos + 1,team1, r)
    visited[nums[pos]] = False
    team1.pop()
    nCr(pos + 1, team1, r)

nCr(0,[],selected)
print(min_val)



