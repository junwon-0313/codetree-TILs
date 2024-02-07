N, M = map(int, input().split())
graph = [[0]*M for _ in range(N)]

dy, dx = [0,1,0,-1], [1,0,-1,0]
x, y,di = 0,0,0
for num in range(1, N*M+1):
    # 값을 채움
    graph[x][y]=num
    # 다음 위치를 찾음
    nx, ny = x+dx[di], y+dy[di]
    if 0<=nx<N and 0<=ny<M and graph[nx][ny]==0:
        x, y = nx, ny
    else:
        di = (di+1)%4
        x, y = x+dx[di], y+dy[di]

for x in range(N):
    for y in range(M):
        print(graph[x][y], end = ' ')
    print()