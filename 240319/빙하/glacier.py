# 0 은 물, 1은 빙하
# 상하 좌우에 빙하가 둘러 쌓인 경우 녹지 않음.
# 모두 녹는데 걸리는 시간
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def no_ice():
    for x in range(n):
        for y in range(m):
            if graph[x][y]==1:
                return False
    return True


# O(n*m max(n,m))
dxs, dys = [1,-1,0,0],[0,0,1,-1]
# 0,0을 시작으로 물이 이어진 부분을 찾음
# 1초 후, 바깥 빙하를 녹임: 방문처리 된 영역 근처라면
def bfs():
    q=[(0,0)]
    visited = [[False]*m for _ in range(n)]
    # visited[0][0]=True
    while q:
        x,y = q.pop(0)
        for dx, dy in zip(dxs,dys):
            nx,ny = x+dx, y+dy
            if not in_range(nx,ny):
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny]==0:
                q.append((nx,ny))
                visited[nx][ny]=True
    return visited

def melt():
    cnt=0
    for x in range(n):
        for y in range(m):
            if graph[x][y]==1:
                for dx, dy in zip(dxs,dys):
                    nx,ny = x+dx, y+dy
                    # 범위 예외처리 안해줘도 됨.
                    if visited[nx][ny]:
                        graph[x][y]=0
                        cnt+=1
                        break
    return cnt
                    

time=0
last_cnt =0
while True:
    time+=1
    visited = bfs()
    last_cnt = melt()

    if no_ice():
        break
 

print(time, last_cnt)