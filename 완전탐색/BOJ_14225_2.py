"""
해당 원소가 포함 된다 안된다 이진으로 표현할 수 있는 비트마스크를 사용
"""

n = int(input())

arr = list(map(int, input().split()))

bit_size = 1 << n

nums = [0] * 2000001


for i in  range(bit_size):
    num = 0
    for k in range(n):
        if i & (1 << k):
            num += arr[k]
    nums[num] = 1
for i in range(len(nums)):
    if not nums[i]:
        print(i)
        break