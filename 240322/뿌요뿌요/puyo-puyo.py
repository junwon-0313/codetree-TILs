# 하나의 블럭 -> 4개 이상 터짐
n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))

dxs, dys = [1,-1,0,0], [0,0,1,-1]
def in_range(x,y):
    return 0<=x<n and 0<=y<n

def dfs(x,y,num):
    global cnt
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if not in_range(nx,ny):
            continue
        if visited[nx][ny]:
            continue
        if graph[nx][ny]==num:
            visited[nx][ny]=True
            dfs(nx,ny,num)
            cnt+=1

visited = [[False]*n for _ in range(n)]
bomb, size = 0, 0
for x in range(n):
    for y in range(n):
        cnt=1
        if not visited[x][y]:
            visited[x][y]=True
            dfs(x,y,graph[x][y])
        size = max(size,cnt)
        if cnt>=4:
            bomb+=1

print(bomb, size)