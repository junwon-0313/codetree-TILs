# 최장 증가 수열
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def print_graph(g):
    global n
    for x in range(n):
        for y in range(n):
            print(g[x][y], end =' ')
        print()
# print_graph(graph)
dp = 0

# dfs를 사용해서 각각의 시작점에서 최대 깊이를 파악
dx, dy = [1,-1,0,0], [0,0,1,-1]
def dfs(x,y, visited, cnt):
    visited[x][y]=True
    global dp
    if cnt> dp:
        dp = cnt
    for idx in range(4):
        nx, ny = x+dx[idx], y +dy[idx]
        # 범위 초과
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        # 방문하지 않았고 증가할 수 있는 좌표가 있을 경우
        if not visited[nx][ny] and graph[nx][ny]>graph[x][y]:
            dfs(nx,ny, visited, cnt+1)


# 모든 시작점에 대해서 dfs 2500*2500*4 
for x in range(n):
    for y in range(n):
        dfs(x,y, [[False]*n for _ in range(n)], 1)
print(dp)