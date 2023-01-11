import sys
si = sys.stdin.readline

flag = True


def nCr(pos,a,original,n,r):
    if pos == n:
        if len(a) == r:
            for num in a:
                print(num , end= ' ')
            print()
        return
    a.append(original[pos])
    nCr(pos+1,a,original,n,r)
    a.pop()
    nCr(pos+1,a,original,n,r)


while flag:
    arr = list(map(int,input().split()))
    if len(arr) == 1 and arr[0] == 0:
        break
    else:
        new_arr = arr[1:]
        nCr(0,[],new_arr,arr[0],6)
        print()
