import sys
from collections import defaultdict
si = sys.stdin.readline
dance_names = defaultdict(int)
dance_names['ChongChong'] = 1
n = int(si())
for _ in range(n):
    a,b = si().split(' ')
    a = a.replace("\n","")
    b = b.replace('\n',"")
    if dance_names[a] == 1 or dance_names[b] == 1:
        dance_names[a] = 1
        dance_names[b] = 1
ans = 0
for value in dance_names.values():
    if value > 0 :
        ans += 1

print(ans)