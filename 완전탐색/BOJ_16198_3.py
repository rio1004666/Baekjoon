"""
3. 분할-정복 기법으로 풀기
5
100 2 1 3 100
"""

n = int(input())
bids = list(map(int, input().split()))

def divide_conquer(arr):
    if len(arr) == 3:
        return arr[0]*arr[2]

    ret = 0 # 최댓값 0부터 시작함
    for i in range(1, len(arr) - 1):
        # 현재 i번째 구슬을 선택하고 에너지를 계산한 뒤 나머지 구슬들을 대상으로 다시 탐색들어감
        ret = max(ret,arr[i-1]*arr[i+1] + divide_conquer(arr[:i]+arr[i+1:]))
    return ret

ans = divide_conquer(bids)
print(ans)




