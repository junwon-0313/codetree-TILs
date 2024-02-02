global n, m
n,m = map(int,input().split())

# 진행하다가 길이 막혔을 때, 방향을 시계 방향으로 90도 회전
# 우, 하 ,좌, 상
dx, dy = [0,1,0,-1], [1,0,-1,0]

# 격자를 벗어나지 않는지 + 이미 방문
graph = [[0]*m for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<m

idx = 0
x,y = 0,0
for count in range(1, n*m+1):
    # 값 할당
    graph[x][y]=count
    # 방향 바꾸기
    nx, ny = x+dx[idx], y+dy[idx]
    if in_range(nx,ny) and graph[nx][ny]==0:
        x, y = nx,ny
    else:
        idx= (idx+1)%4
        x,y= x+dx[idx], y+dy[idx]


for x in range(n):
    for y in range(m):
        print(graph[x][y], end = ' ')
    print()