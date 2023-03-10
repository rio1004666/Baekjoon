"""
문제
예술을 사랑하는 사람들이 시장에 모여서 그들의 그림을 서로 거래하려고 한다. 모든 그림의 거래는 다음과 같은 조건을 만족해야 한다.

그림을 팔 때, 그림을 산 가격보다 크거나 같은 가격으로 팔아야 한다.
같은 그림을 두 번 이상 사는 것은 불가능하다.
방금 시장에 새로운 그림이 들어왔다. 1번 아티스트는 그 그림을 외부 상인에게 가격 0을 주고 샀다. 이제 그 그림을 자신의 예술가 친구들에게 팔려고 한다. 위의 조건을 모두 만족하는 거래만 이루어진다고 가정했을 때, 그림을 소유했던 사람의 수의 최댓값을 출력하는 프로그램을 작성하시오. (1번 아티스트와 마지막으로 그 그림을 소유한 사람도 포함한다).

입력
첫째 줄에 예술가의 수 N이 주어진다. N은 2보다 크거나 같고, 15보다 작거나 같은 자연수이다.

둘째 줄부터 N개의 줄에는 N개의 수가 주어진다. i번째 줄의 j번째 수는 j번 예술가가 i번 예술가에게 그 그림을 살 때의 가격이다. 모든 가격은 0이 제일 낮은 가격이고, 9가 제일 높은 가격이다.

문제 이해 및 구하고자하는것을 파악해야한다
해결방식도 완전탐색으로 먼저해본다
1번아티스트가 그림을 0에 주고 사는것부터 시작하고
1번아티스트의 그림을 2번아티스트가 살대, 3번아티스트가 살때 각각 경우의 수가 있다
2번아티스트의 그림을 1번아티스트가 살경우, 3번아티스트가 사는 경우
3번아티스트의 그림을 1번아티스트가 살 경우 2번아티스트가 사는 경우
자기자신이 사는 경우는 0이다 (당연함)

예제 파악
2번아티스트가 1번한테서 그림을 사는 경우 2를 주고 산다
그다음 2번이 가지고 있는 그림을 1번이나 3번이 살 수 있다? 아니다 문제 조건에서 산가격 이상을 지불해야만 살 수 있으므로
3번이 1번한테 사든 2번이 1번한테 사든 그 이후로 그림을 살 수는 없으므로 처음 1번아티스트가 가지고 있을 때 그림과 2번이 사든 3번이 사든 한사람만
그림을 가지고 있을 수 있으므로 총 2명이 최대로 그림을 가질 수 있었던 경우의 수가 된다

또 조건에 한번 그림을 가졌던 사람은 더이상 그 그림을 살 수 없다고 하였으므로 한번이라도 그림을 샀던 사람을 방문체크해주어야 한다( 기록 )

그리고 총 인원이 15명으로 지극히 n이 작다

완전탐색을 이용한 비트마스킹 dp 로 해결 할 수 있다

그림을 산 최대사람수는 재귀형태로 탐색하여 경우의수를 찾을 수 있고

그림을 샀다라는 것을 기록하는 방법은 비트마스킹을 사용 할 수 있다

테이블 정의
dp[현재아티스트][현재까지그림을구매한사람체크][현재아티스트가구매했던 그림가격]
= 현재아티스트가 그림을 팔 떼 가장 많은 사람에게 그림을 팔 수 있는 경로의 사람의 수 = 부분문제로 쪼개서 다음문제를 해결할 수 있음

기억이 필요한 인수 세가지가 필요함 현재 가리키는 아티스트번호 cur , 각 방문을 한번씩만 해야함을 표시하는 visited , 이전에 구매했던 가격 이 세가지를 기억해야만
그 다음 문제를 풀 수 있음

이 문제는 조건에 따라 팔 수 있는 방법이 정해져있으므로 모든 경우의수를 구한 후 그 중 최댓값을 구하는 문제이다

완탐으로는 복잡한 경우의 수이므로 다이나믹 프로그래밍으로 푸는것이 가장 해결하기 쉬운 문제이다
1번 아티스트에서 2번아티스트로 가던가 1번아티스트에서 3번으로 가던가 ( 0이라서 처음에는 다 가능한 경우이다 )
2번아티스트에서 1번으로 갈 수는 없다 ( 조건2 ) 2번아티스트에서 3번아티스로 혹은 4번 혹은 5번이 구매할수도있지만 조건1에 의해서 정해져있다

이번문제에서 그림을 그려가며 어떤부분이 기존의 작은문제이고 그다음문제를 해결할 수 있느 다이나믹 프로그래밍 문제인지 파악해야한다
1번 -> 2번 -> 3번...
1번 -> 3번 -> 2번...
1번 -> 4번 -> 2번...
1번 -> 5번 -> 3번....
2번의 입장에서 1번 -> 3번을 통해 구매를 할 수 있고 1번 -> 4번을 통해 구매를 할수도있다 왜냐 구매하는 가격이 다르기 때문에 다른 경로를 설정해야한다
그리고 가장 취약한 나의 재귀함수 리턴값 표현인데
이것도 그래프 형식으로 그려보고 펼치면

각 경로의 최댓값을 모아서 다시 최댓값을 구하여 리턴하고
또 각각의 경우에 대해 최댓값을 모아서 최댓값을 구하여 리턴하는 방식을 확인한다면 충분히 구현할 수 있다

이 문제는 외판원순환문제와 비슷하고 경로의 경우의수를 구하는문제와 비슷하다 매우
얼핏보기에는 사고파는 과정이 간선으로 보이지 않지만 간선으로 본다면 그래프의 dfs탐색문제와 비슷하다

"""

n = int(input())
slist = []
for _ in range(n):
    arr = list(map(int, input()))
    slist.append(arr)
dp = [[[0] * 10 for _ in range(1<<n)] for _ in range(n) ]


def dfs(cur, visited , price):
    # 전부 방문한 파라미터라면 그대로 리턴한다 ( 메모제이션 ) => 횟수는 같기때문이다
    if dp[cur][visited][price] != 0:
        return dp[cur][visited][price]

    count = 0
    # 2번아티스트부터 구매한다
    for nexta in range(1,n):
        # 다음 아티스트가 구매하는 비용이 현재 구매한 비용보다 작아야 한다
        # 또 다음 방문할 아티스트가 이미 그림을 산적이 있다면 건너뛴다
        if slist[cur][nexta] < price or visited & (1<<nexta) > 0:
            continue
        count = max(count,1 + dfs(nexta,visited | (1<<nexta), slist[cur][nexta]))
    # 위에서 한데 모은 최대 구매사람수를 기록한다 최종적으로
    dp[cur][visited][price] = count
    return count
# 1번 아티스트 포함한다
ans = 1 + dfs(0,1,0) # 현재위치는 0번 , 방문인덱스번호는 1번 , 구매한 가격은 0이다
print(ans)



