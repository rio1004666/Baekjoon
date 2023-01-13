import sys

n = int(input())

arr = list(map(int, input().split()))

ops = list(map(int, input().split()))

max_val = -sys.maxsize
min_val = sys.maxsize

def go(pos,total):
    global max_val,min_val

    if pos == n:
        max_val = max(max_val,total)
        min_val = min(min_val,total)
        return
    if ops[0] > 0:
        ops[0] -= 1
        go(pos+1,total + arr[pos])
        ops[0] += 1
    if ops[1] > 0:
        ops[1] -= 1
        go(pos+1, total - arr[pos])
        ops[1] += 1
    if ops[2] > 0:
        ops[2] -= 1
        go(pos+1, total * arr[pos])
        ops[2] += 1
    if ops[3] > 0:
        ops[3] -= 1
        go(pos+1, int(total / arr[pos]))
        ops[3] += 1

go(1,arr[0])
print(max_val)
print(min_val)