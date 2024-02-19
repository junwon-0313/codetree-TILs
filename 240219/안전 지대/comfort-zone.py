# K 이하인 집들은 모두 비가 오면 잠김
# 안전영역: 잠기지 않은 집들
#-> 동일한 안전지역
# 안전 영역의 수가 최대가 될 때의 K와 그 수
n,m = map(int, input().split())
town = [list(map(int,input().split())) for _ in range(n)]
dxs , dys = (0,0,1,-1), (1,-1,0,0)

def find_k():
    num_lst = set()
    for x in range(n):
        for y in range(m):
            num_lst.add(town[x][y])
    return list(num_lst)

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def dfs(x,y,k): # 상하좌우
    for dx, dy in zip(dxs,dys):
        nx,ny = x+dx, y+dy
        if not in_range(nx,ny):
            continue
        if visited[nx][ny]:
            continue
        if town[nx][ny]>k:
            visited[nx][ny]=True
            dfs(nx,ny,k)

# 가능한 k값을 모두 찾기
num_lst = find_k()
num_lst.sort()
# print(num_lst)

total = []

for k in num_lst:
    visited = [[False]*m for _ in range(n)]
    town_num =0
    for x in range(n):
        for y in range(m):
            if visited[x][y]:
                continue
            if town[x][y]>k:
                visited[x][y]=True
                town_num+=1
                dfs(x,y,k)

    total.append((k,town_num))

total = sorted(total, key=lambda x:(-x[1],x[0]))
print(total[0][0], total[0][1])