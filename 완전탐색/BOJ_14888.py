""""
N <= 10
원소범위 <= 100

연산자를 하나씩 써가며 최댓값과 최솟값을 업데이트한다

완전 탐색 4^10 = 2^20 = 100^4 = 100만 => 가능하다

"""

# import sys
#
# n = int(input())
# arr = list(map(int, input().split()))
# op = list(map(int,input().split()))
# oplist = []
# # 먼저 연산자들을 그냥 싹다 담아서 완전탐색을 진행한다
# # 어차피 연산자의 최대 개수는 10개다 (n이 11개이기 때문)
#
# for i,num in enumerate(op):
#     if i == 0:
#         for j in range(num):
#             oplist.append('+')
#     elif i == 1:
#         for j in range(num):
#             oplist.append('-')
#     elif i == 2:
#         for j in range(num):
#             oplist.append('*')
#     else:
#         for j in range(num):
#             oplist.append('/')
#
# op_size = n-1
# visited = [0] * (n-1)
# 답이 틀렷네 ? 내가 간과하고있는 경우가 어떤거일까를 생각해봣거든?
# 최댓ㄱ
# 최대값이 음수가 나올수잇구나? ...................
# 그럼 최댓값 셋팅을 음수로 극한을 줘야겟군....???
# -만 나오는 경우 그럴수 있어..............
# max_val = -sys.maxsize
#
# min_val = sys.maxsize
# def go(index, calc_ans):
#     global max_val , min_val
#     if index == n:
#         max_val = max(max_val,calc_ans)
#         min_val = min(min_val,calc_ans)
#         return
#
#     for i in range(op_size):
#
#         if visited[i] == 1: continue
#         if oplist[i] == '+':
#             visited[i] = 1
#             go(index + 1, calc_ans + arr[index])
#             visited[i] = 0
#         elif oplist[i] == '-':
#             visited[i] = 1
#             go(index + 1, calc_ans - arr[index])
#             visited[i] = 0
#         elif oplist[i] == '*':
#             visited[i] = 1
#             go(index + 1, calc_ans * arr[index])
#             visited[i] = 0
#         else:
#             visited[i] = 1
#             temp = calc_ans // arr[index]
#             if calc_ans < 0:
#                 temp = calc_ans * (-1)
#                 temp = (temp // arr[index]) * (-1)
#             go(index + 1, temp)
#             visited[i] = 0
# go(1,arr[0])
#
# print(max_val)
# print(min_val)


"""

위의 풀이는 10^10이므로 시간복잡도 말도 안되게 오래 걸린다 
그렇다면 어떻게 줄일 수 있을까 ?
연산자들을 하나씩 담아서 넣어보는것이 아니라 갯수를 카운트다운시키며 넣어본다 
획기적인 시간단축이다;;;;;

"""
import sys
n = int(input())
arr = list(map(int, input().split()))
plus,minus,multiply,divide = map(int, input().split())
max_val = -sys.maxsize
min_val = sys.maxsize



def go(pos, acc):
    global max_val, min_val
    global plus,minus,multiply,divide
    if pos == n:
        max_val = max(max_val,acc)
        min_val = min(min_val,acc)
        return
    else:
        if plus > 0:
            plus -= 1
            go(pos+1, acc + arr[pos])
            plus += 1
        if minus > 0:
            minus -= 1
            go(pos + 1, acc - arr[pos])
            minus += 1
        if multiply > 0:
            multiply -= 1
            go(pos + 1, acc * arr[pos])
            multiply += 1
        if divide > 0:
            divide -= 1
            go(pos + 1, int(acc / arr[pos]))
            divide += 1
go(1,arr[0])

print(max_val)
print(min_val)




