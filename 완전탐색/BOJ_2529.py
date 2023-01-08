"""
부등호에 맞는 숫자를 모두 구한다

예를들어 <>라면
0 < 2 > 1 만족하고
1 < 4 > 3 만족하고
....
8 < 9 > 7 만족한다
이 모두를 구하고 정렬한 다음 가장 큰수와 작은수를 구한다
그리고 이미 쓴 숫자는 쓸 수 없으므로 방문처리한다
완전탐색으로 구하면 되는가? 시간상?
가능하다 왜냐면
10! 이된다
0부터 9까지 숫자 10개중에 하나를 선택하면
나머지 9개 중 하나를 골라야 한다
또 나머지 8개중 하나를 골라야 한다



"""

def ok(x,y,op):
  if op == '<':
    if x > y:
      return False
  if op == '>':
    if x < y:
      return False

  return True
def go(index , nums):
  global cnt
  if index == k + 1:
      ans.append(nums)
      return
  for i in range(10):
    cnt += 1
    if check[i]:continue
    if index == 0 or ok(nums[index-1],str(i),arr[index-1]):
      check[i] = True
      go(index + 1, nums + str(i))
      check[i] = False

k = int(input())
arr = input().split()
check = [False] * 10
ans = []
cnt = 0
go(0,'')
ans.sort()
print(cnt)
print(ans[-1])
print(ans[0])