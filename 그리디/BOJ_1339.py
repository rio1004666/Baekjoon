# 단어수학문제를 파이썬으로 순열 백트래킹으로 푸니까 시간 초과
# 그래서 다른 풀이로도 가능한가?
# 가능하고 시간복잡도도 현저히 낮다면 그렇게 푸는것이 맞다
# 그리디하게 푼다

n = int(input())
arr = [0] * 26
slist = []
for _ in range(n):
    string = input()
    l = len(string) - 1
    # 같은 자리의 알파벳이라도 다른 자리에 한번더 등장하면 우선순위를 높게 줌
    for s in string:
        arr[ord(s) % 65] += 10**l # 각 알파벳별로 가중치를 계산하는작업
        l -= 1
arr.sort(reverse=True)# 정렬해서 차례대로 9부터 1까지 부여함
result = 0
for i,j in zip(arr,range(9,0,-1)):
    result += i*j
print(result)