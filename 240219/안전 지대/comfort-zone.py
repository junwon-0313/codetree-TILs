# 최대 재귀 깊이를 설정
import sys
# 맵의 최대 크기가 2500이므로 2500번 반복 가능!
# 10**6은 메모리 에러, 그 이상은 OverflowError 
sys.setrecursionlimit(2000) 


n,m = map(int, input().split())
town = [list(map(int,input().split())) for _ in range(n)] # 집의 높이 graph

def in_range(x,y):
    return 0<=x<n and 0<=y<m

dxs , dys = [0,0,1,-1], [1,-1,0,0]
def dfs(x,y,k):
    for dx, dy in zip(dxs,dys): # 상하좌우: 인접 체크
        nx,ny = x+dx, y+dy
        if not in_range(nx,ny): # 범위를 초과하면 pass
            continue
        if visited[nx][ny]: # 이미 방문했으면 pass
            continue
        if town[nx][ny]>k: # 물에 잠기지 않은 집만 계속 탐색
            visited[nx][ny]=True
            dfs(nx,ny,k)

total = []

for k in range(1,101): # 비가 온 높이마다 마을 수 체크
    visited = [[False]*m for _ in range(n)] # 방문 처리
    town_num =0
    for x in range(n):
        for y in range(m):
            if not visited[x][y] and town[x][y]>k: # 방문하지 않았고 물에 잠기지 않았을 때
                visited[x][y]=True
                town_num+=1
                dfs(x,y,k)

    total.append((k,town_num))

total = sorted(total, key=lambda x:(-x[1],x[0]))
print(total[0][0], total[0][1])