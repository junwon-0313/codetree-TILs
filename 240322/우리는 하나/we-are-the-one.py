n, k, u, d = map(int,input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

dxs, dys = [1,-1,0,0], [0,0,1,-1]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def bfs(x,y):
    q =[]
    q.append((x,y))
    visited[x][y]=True
    available_num =1
    while q:
        x,y = q.pop(0)
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if not in_range(nx,ny):
                continue
            if visited[nx][ny]:
                continue
            # 두 도시간의 높이의 차가 u이상 d이하 경우
            if u<=abs(graph[x][y]-graph[nx][ny])<=d:
                q.append((nx,ny))
                visited[nx][ny]=True
                available_num+=1
    return available_num
# 최대로 이동가능한 도시 수
city_lst =[]
visited = [[False]*n for _ in range(n)]
for x in range(n):
    for y in range(n):
        if not visited[x][y]:
            city_lst.append(bfs(x,y))

city_lst.sort(reverse = True)
ans =0
for idx in range(k):
    ans+=city_lst[idx]
print(ans)