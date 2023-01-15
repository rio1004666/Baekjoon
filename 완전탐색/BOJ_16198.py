"""

에너지 구술 하나씩 제거해보는 완전탐색 알고리즘을 사용
구슬이 10개뿐
제거하는 부분을 링크드리스트로 써도 될것이다 하지만
개수가 매우 작기때문에 비트마스킹을 써도 되고
방문체크해도 될것이다
혹은 그냥 리스트에 담아두고 하나씩 제거해봐도 될것이다
여기서 포인트는 제거해본다 하나씩 -> 완전탐색
우선 모든 순열을 생각해보자 첫번재랑 마지막은 고를 수 없으므로
두번째부터 고르고 그다음 세번째고른 다음
최댓값 구하고.. 브루트포스 -> 백트래킹 + 가지치기

1. 한구슬씩 선택한거 체크하면서 풀기

"""

n = int(input())
arr = list(map(int, input().split()))
checked = [0] * n

ans = 0
def get_energy(idx):
    left,right = idx-1,idx+1 # 자신을 기준으로 왼쪽 오른쪽으로 나눈다
    w1,w2 = arr[left],arr[right] # 에너지구슬이 왼쪽 오른쪽부터 시작된다
    while left >= 0:
        # 선택된 구슬은 제거되고 체크안된 구슬을 발견하면 그것을 선택한다
        if not checked[left]:
            w1 = arr[left]
            break
        left -= 1
    # 왼쪽 오른쪽 구슬들 모두 본다
    while right <= n-1:
        if not checked[right]:
            w2 = arr[right]
            break
        right += 1
    return w1*w2

def select_bids(pos,accum):
    global ans
    if pos == n-1:
        ans = max(ans, accum)
    for i in  range(1,n-1):
        if checked[i]:continue
        checked[i] = True
        w = get_energy(i)
        select_bids(pos+1,accum + w)
        checked[i] = False


select_bids(1,0)
print(ans)








