"""
배운 알파벳을 비트마스킹으로 처리하여
비트연산 &을 사용하여 교집합으로 포함되어 성립하면 카운팅하면 됨
"""

from itertools import combinations
import sys

si = sys.stdin.readline
n, k = map(int, input().split()) # n,k를 입력받음

words = [0] * n # 각 단어별로 비트마스킹으로 표현된 2진수값을 - 2^k로 표현됨

# 단어들을 입력받음
for i in range(n):
    word = si().rstrip()
    # 각 단어별로 사용된 알파벳을 비트로 켜서 표현함
    for w in word:
        words[i] |= (1 << (ord(w) - ord('a')))
# 일반적으로 2^n - 1 의 값까지 10진수를 2진수 비트로 표현하여 해당 원소를 선택했다면 비트가 1로 & 연산을 했을 경우 1이 되어 계산하는 방식이다
# 이제 알파벳 26개 중에 k를 선택하여 각 단어를 읽을 수 있는지만 체크할 것이다
candidiate = ['b','d','e','f','g','h','j','k','l','m','o','p','q','r','s','u','v','w','x','y','z']
need = ['a','c','t','i','n']

ans = 0
if k < 5:
    print(0)
    exit(0)

for teach in list(combinations(candidiate,k-5)):

    # 알파벳 K개를 선택하엿음
    # 이제 비트마스킹을 하여 2진수를 10진수로 표현함
    current = 0
    cnt = 0
    # 필요한것 외에 비트마스킹
    for t in teach:
        current |= (1 << (ord(t) - ord('a')))
    # 필요한 것들 비트마스킹
    for t in need:
        current |= (1 << (ord(t) - ord('a')))
    # 각 단어를 돌아다니면서 단어를 읽을 수 있는지 판단한다
    # 읽을 수 있는지 판단하기 위해서는 비트연산 교집합으로 자기 자신이 전부 나오게 된다면 그 단어에 해당하는 알파벳이 모두 존재한다는 의미이므로 읽을 수 잇다고 판단한다
    for w in words:
        if w & current == w:
            cnt += 1
    ans = max(ans , cnt)


print(ans)