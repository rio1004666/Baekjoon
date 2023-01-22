"""
효율적인 풀이
set을 이용해서 이미 방문한 알파벳을 거른다
어차피 배열로 체크해도 복잡도 1로 체크 할 수 있는데 .... dfs 는 시간초과 나는거같다
bfs 로 푸는것도 좋은 방법이다

"""
r,c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
visited = set()
dx,dy = (-1,1,0,0),(0,0,1,-1)
ans = 0
def dfs(x,y,cnt):
    global ans
    ans = max(ans,cnt)
    # 일단 해당 칸을 방문함
    visited.add(graph[x][y])
    for i in range(4):
        nx,ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and  0 <= ny < c:
            if graph[nx][ny] not in visited:
                dfs(nx,ny,cnt+1)
    # 다시 원상태로 복구 시켜야함
    visited.remove(graph[x][y])
dfs(0,0,1)
print(ans)