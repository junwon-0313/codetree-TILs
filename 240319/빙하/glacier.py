n, m = map(int, input().split())
graph = []
dxs, dys= [1,-1,0,0], [0,0,1,-1]
for _ in range(n):
    graph.append(list(map(int, input().split())))

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def bfs(x,y, num):
    q = []
    q.append((x,y,num))
    visited = [[False]*m for _ in range(n)]
    visited[x][y]=True # 방문처리
    while q:
        x, y,num = q.pop(0)
        for dx, dy in zip(dxs, dys):
            nx,ny = x+dx, y+dy
            if not in_range(nx,ny):
                continue
            if visited[nx][ny]: # 방문했으면 skip
                continue
            if graph[nx][ny]==0 or graph[nx][ny]==-num+1: # 물이면 
                visited[nx][ny]=True # 방문처리
                q.append((nx,ny,num))
            if graph[nx][ny]==1:
                graph[nx][ny]=-num

def print_graph(graph):
    for x in range(n):
        for y in range(m):
            print(graph[x][y], end =' ')
        print()

def cnt_ice(num):
    cnt =0
    for x in range(n):
        for y in range(m):
            if graph[x][y]==num:
                cnt+=1
    return cnt

time=1
for x in range(n):
    for y in range(m):
        if graph[x][y]==-time+1:
            bfs(x,y,time)
            # print(time)
            # print_graph(graph)
            time+=1
# print_graph(graph)
print(time-2, cnt_ice(-time+2))