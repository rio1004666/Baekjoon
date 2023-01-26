"""
문제이해
단어를 많이 읽게 하기 위해
k개의 글자들을 선택
즉 k개의 단어를 선택하여 최대로 단어들을 읽을 수 있게 하도록
하는 방법이 있따면 그 단어의 개수를 구하기

단어는 anta로 시작 tica로 끝남
그럼 그 사이에 있는 알파벳수가 관건
단어는 8이상 15이하의 길이이고
anta와 tica외에 다른 단어가 포함 되어 있지 않다면
antatica 로 8개 최소를 만족한다

관찰
antatica로 최소 8자리 수가 되고
anta + K개를 뽑은 알파벳 + tica 로 이루어져 있는데
k는 26개까지 뽑을 수 있다 즉
알파벳 소문자 개수가 26개이다
최대로 많은 단어를 읽게하려면
많은단어들이 포함하는 알파벳을 먼저 뽑아야 한다

흠 근데 문제는 기본적으로 깔려있는 antatica
이 단어에서 antic이렇게 5개의 단어를 일단 알아야함
즉 기본적으로 가르쳐야 할 단어가 이 5개의 글자를 가르쳐야함?

이거 이하로 가르치면 아예가르칠 수 없다고 0개가 된다 ?

antarctica
antahellotica
antacartica

여기서 총 6개의 단어를 골라야하는데
antic이렇게 5개를 무조건 뽑아야하고
r을 뽑음으로써 2개를 읽을 수 있다
즉 antarctica 와 antacartica를 읽을 수 있다
antahellotica는 읽지 못한다
이렇게 이해가 되었는데
어떻게 풀 수 있을까?

일단 단어를 읽을 수 있으려면
각 단어가 필요한 알파벳들이 무엇인지 파악할 필요가 있어
그렇게 가장 많이 필요로 하는 글자들을 쭉 나열한 후에
정렬해서 가장 많이 필요로하는 알파벳들부터 선택해나가는거지


근데 문제는....
최대 빈도수 글자부터 선택해도
그 단어를 읽으려면 온전히 나머지 글자도 선택해야만해
흠 그냥
선택하면 될까?
가장 많이 사용되는 알파벳을 골라서 선택하고
그다음 많이 사용되는 알파벳을 고르는게...
그렇게 해도 가장 많이 사용되는 알파벳을 골라도
그 글자를 읽을 수 없으면 도루묵이거든?

그래서 ...흠 완전탐색으로 알파벳 26개중에 그냥
k-5개를 고르는거야
그리고 단어들을 몇개 읽을 수 있을지 체크후 업데이트 하는거지

조합의 경우의 수가 최대 개수는 1000만이야...
여기서 단어의 개수가 최대 50개니까...


"""
from itertools import combinations
import sys
si = sys.stdin.readline
n,k = tuple(map(int, input().split()))
first_selected = {'a','n','t','i','c'}
remain_selected = set(chr(i) for i in range(97,123)) - first_selected
data = [si().rstrip()[4:-4] for _ in range(n)]

def countReadableWord(data,learned):
    cnt = 0
    # 단어를 읽을 수 있는지 체크하기 위해 함수를 만듬
    for d in data:
        flag = 1
        for w in d:
            idx = ord(w) - ord('a')
            # 이 단어에 배우지 않은 글자가 있다면 즉시 못읽는다며 빠져나온다
            if not learned[idx]:
                flag = 0
                break
        if flag:
            cnt += 1
    return cnt
if k >= 5:
    ans = 0
    learned = [0] * 26
    # 이미 배운것은 체크한다
    for x in first_selected:
        idx = ord(x) - ord('a')
        learned[idx] = 1
    # 남은 알파벳중에서 k-5개를 선택해본다.
    for teach in list(combinations(remain_selected,k-5)):
        for t in teach:
            idx = ord(t) - ord('a')
            learned[idx] = 1
        cnt = countReadableWord(data,learned) # 반복되고 코드읙 길이가 길어지고 파라미터만 넘겨줘도 된다고 생각하면 함수로 뺀다
        # 체크해놓은 알파벳들을 다시 원래대로 해놓는다 => 백트래킹
        for t in teach:
            idx = ord(t) - ord('a')
            learned[idx] = 0
        ans = max(ans,cnt)
    print(ans)
else:
    print(0)