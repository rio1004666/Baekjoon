n = int(input())
arr =[]
s = set()
d = {}
for _ in range(n):
    a = list(input())
    for i in a:
        s.add(i)
    arr.append(a)

size = len(s)
slist = list(s)
slist.sort()

check = [0] * (10)
ans = []
fin = 0
def calc():
    global fin
    # 각 알파벳에 숫자를 셋팅해준다
    for i,k in enumerate(slist):
        d[k] = ans[i]
    # 모든 단어를 숫자로 변환해 준다
    ret = 0
    for a in arr:
        t = ''
        for i in a:
            t += str(d[i])
        ret += int(t)
    fin = max(fin,ret)
def dfs(pos):
    if pos == 10:
        calc()
        return

    for i in range(10-size,10):
        if check[i]:continue
        check[i] = 1
        ans.append(i)
        dfs(pos+1)
        check[i] = 0
        ans.pop()
dfs(10-size)
print(fin)





