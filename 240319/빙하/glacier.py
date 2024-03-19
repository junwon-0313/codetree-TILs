# 0 은 물, 1은 빙하
# 상하 좌우에 빙하가 둘러 쌓인 경우 녹지 않음.
# 모두 녹는데 걸리는 시간
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def remain_ice():
    cnt=0
    for x in range(n):
        for y in range(m):
            if graph[x][y]==1:
                cnt+=1
    return cnt


# 200*200*4*200
dxs, dys = [1,-1,0,0],[0,0,1,-1]
# 0,0을 시작으로 물이 이어진 부분을 찾음
# 1초 후, 바깥 빙하를 녹임: 방문처리 된 영역 근처라면
def bfs(x,y, graph):
    tmp_graph = [i[:] for i in graph]
    q=[]
    q.append((x,y))
    visited = [[False]*m for _ in range(n)]
    while q:
        x,y = q.pop(0)
        visited[x][y]=True
        for dx, dy in zip(dxs,dys):
            nx,ny = x+dx, y+dy
            if not in_range(nx,ny):
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny]==0:
                q.append((nx,ny))
                visited[nx][ny]=True
            if graph[nx][ny]==1:
                tmp_graph[nx][ny]=0
    return tmp_graph

def print_graph(graph):
    print('GRAPH')
    for x in range(n):
        for y in range(m):
            print(graph[x][y], end = ' ')
        print()

cnt_lst=[]
time=0
visited = [[False]*m for _ in range(n)] 
while True:
    # print_graph(graph)
    cnt = remain_ice()
    if cnt ==0:
        break
    cnt_lst.append(cnt)
    time+=1
    graph = bfs(0,0, graph)
    

print(time, cnt_lst[-1])