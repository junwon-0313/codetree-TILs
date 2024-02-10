N,M = map(int, input().split())
alpha = [chr(i) for i in range(65,91)]
dx, dy = [0,1,0,-1], [1,0,-1,0]

graph = [[0]*M for _ in range(N)]
idx, x, y = 0, 0, 0
def in_range(x,y):
    return 0<=x<N and 0<=y<M

for num in range(N*M):
    graph[x][y] =alpha[num%26]
    nx, ny = x + dx[idx], y + dy[idx]
    if in_range(nx,ny) and graph[nx][ny]==0:
        x,y = nx,ny
    else:
        idx= (idx+1)%4
        x,y = x + dx[idx], y + dy[idx]

for x in range(N):
    for y in range(M):
        print(graph[x][y], end = ' ')
    print()