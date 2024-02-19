from collections import deque

n, k = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

start_lst = [list(map(int, input().split())) for _ in range(k)]


def in_range(x,y): 
    return 0<=x<n and 0<=y<n

dxs, dys = [0,0,1,-1], [1,-1,0,0]
def bfs(r, c):
    global total
    q = deque()
    q.append((r,c))
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx,ny = x+dx, y+dy
            if not in_range(nx,ny):
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny]==0:
                visited[nx][ny]=True
                total+=1
                q.append((nx,ny))


visited = [[False]*n for _ in range(n)]
total=0
for r, c in start_lst:
    r,c=r-1,c-1
    if visited[r][c]:
        continue
    visited[r][c]=True
    total+=1
    bfs(r,c)

print(total)