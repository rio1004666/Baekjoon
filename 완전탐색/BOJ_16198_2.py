"""
2. 실제로 제거해나가며 풀이
list는 골라진 요소를 삭제하면 나머지 요소들이 빈 자리를 메꾸기 위해 이동하므로 시간소요 증가
DFS에 골라진 요소를 제외한 앞부분의 list, 뒷부분의 list를 합한 리스트를 보내면 해결

"""
import sys

si = sys.stdin.readline
n = int(si())
weights = list(map(int, si().split()))
ans = 0

def backtracking(accum):
    global ans
    if len(weights) == 2:
        ans = max(ans ,accum)
    for i in  range(1,len(weights)-1):
        target = weights[i-1]* weights[i+1]
        # backtracking
        value = weights.pop(i) # 리스트 중간에 값을 뺄때 해당 위치를 파라미터로 넣어줘도 됨
        backtracking(accum + target) # 에너지 계산한 값을 넣어줌
        weights.insert(i,value) # 리스트 중간에 값을 넣을때 해당 값과 인덱스를 넣어주면 됨
backtracking(0)
print(ans)

