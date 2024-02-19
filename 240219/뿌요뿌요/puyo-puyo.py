n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
# 상하좌우 + 같은 수: 하나의 블럭, 4개 이상이면 터짐
# 터지는 블럭의 수와 최대 블럭의 크기
def in_range(x,y):
    return 0<=x<n and 0<=y<n

dxs, dys = [1,-1,0,0], [0,0,1,-1]
def dfs(x,y, num):
    global cnt
    for dx,dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if not in_range(nx,ny):
            continue
        if visited[nx][ny]:
            continue
        if graph[nx][ny]==num:
            cnt+=1
            visited[nx][ny]=True
            dfs(nx,ny, num)

blocks = []
visited = [[False]*n for _ in range(n)]
for x in range(n):
    for y in range(n):
        if not visited[x][y]:
            cnt = 1
            visited[x][y]=True
            dfs(x,y,graph[x][y])
            blocks.append(cnt)

bomb_num =0
for block_num in blocks:
    if block_num>=4:
        bomb_num+=1

# 폭파 블록 수, 블록을 이루는 개수의 최대값
print(bomb_num, max(blocks))