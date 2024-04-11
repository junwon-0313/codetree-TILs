n, m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
target = [(-1,-1)]
for _ in range(m):
    x, y = map(int,input().split())
    target.append((x-1,y-1))

dxs, dys = [-1,0,0,1], [0,-1,1,0] # 상 좌 우 하: 우선 순위
def in_range(x,y):
    return 0<=x<n and 0<=y<n
def find_basecamp(t): # 목적지 편의점과 가까운 베이스 캠프 찾기
    temp_base = []
    for x,y in basecamp:
        if graph[x][y]==-1:
            continue
        temp_base.append((abs(t[0]-x)+abs(t[1]-y), x,y))
    _,base_x,base_y = sorted(temp_base, key=lambda x:(x[0],x[1],x[2]))[0]
    return (base_x, base_y)

def find_route(k):
    q = []
    q.append((guest[k],[]))
    visited =[[False]*n for _ in range(n)]
    visited[guest[k][0]][guest[k][1]]=True
    while q:
        s, r = q.pop(0)
        x, y = s
        if (x,y) == target[k]:
            return r[0]
        for dx,dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if not in_range(nx,ny):
                continue
            if graph[nx][ny]==-1:
                continue
            if visited[nx]ny]:
                continue
            r.append((nx,ny))
            q.append(((nx,ny),r[:]))
            visited[nx][ny]=True
            r.pop()

    return


basecamp = [] # 베이스 캠프 관리
for x in range(n):
    for y in range(n):
        if graph[x][y]==1:
            basecamp.append((x,y))
cnt, time=0,0 # 편의점 도착시
arrived = [False for _ in range(m+1)] # 목적지 도착
guest = [(-1,-1) for _ in range(m+1)]
while True:
    time+=1
    change_lst =[]
    if cnt==m:
        print(time)
        break
    # 이동가능한 사람 중에서 최단 거리 찾기
    for t in range(1,min(m+1,time+1)):
        if arrived[t]: # 방문했다면
            continue
        if guest[t]==(-1,-1): # t==time # 손님이 입장 전이라면 가까운 베이스 캠프로 입주 후, 이동
            base_x, base_y = find_basecamp(target[t])
            guest[t] = (base_x,base_y)
            change_lst.append((base_x,base_y))
        # guest가 원하는 편의점으로 이동할 때, 다음 좌표를 찾음
        nx, ny = find_route(t)
        # 다음 좌표가 도착 편의점이라면 ->
        if (nx, ny)== target[t]:
            arrived[t]=True
            change_lst.append((nx,ny))
            cnt+=1
        else:
            guest[t] = (nx,ny)
    for x, y in change_lst:
        graph[x][y]=-1