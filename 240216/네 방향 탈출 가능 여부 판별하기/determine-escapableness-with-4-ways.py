# bfs: queue 자료구조
# queue가 empty가 될 때까지 동작
# 전부 방문, 재방문x
from collections import deque

n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dxs, dys = [1,-1,0,0], [0,0,1,-1]

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def bfs(start):
    q= deque()
    q.append(start)
    while q:
        x, y = q.popleft()
        if x==n-1 and y==m-1:
            return True
        for dx,dy in zip(dxs, dys):
            nx,ny =x+dx, y+dy
            if not in_range(nx,ny):
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny]==0:
                continue

            visited[nx][ny]=True
            q.append((nx,ny))
    return False

pos = bfs((0,0))

if pos:
    print(1)
else:
    print(0)