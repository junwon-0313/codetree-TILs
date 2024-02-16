# 조건: 시작 위치 -> x보다 작은 모든 곳
# 그 중 최댓값으로 이동
# 여러개일 경우, 행, 열 순으로 작은 순
# 시작 위치 바뀜
# 이렇게 k번 or 더이상 이동 불가 시에 종료
from collections import deque
n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
r, c =map(int, input().split()) # 초기 위치
r, c = r-1, c-1

dxs, dys = [1,-1,0,0], [0,0,1,-1]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

# 자기보다 작은 곳으로만 이동, 그 중 최댓값과 최댓값의 좌표를 갱신
def bfs(x,y):
    max_num, max_r, max_c =0, 1000, 1000
    q = deque()
    q.append((x,y))
    pivot = graph[x][y]
    visited = [[False]*n for _ in range(n)]
    while q:
        x,y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if not in_range(nx,ny):
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny]>=pivot:
                continue
            visited[nx][ny]=True # 방문처리
            if graph[nx][ny]>max_num:
                max_num=graph[nx][ny]
                max_r, max_c = nx,ny
            elif graph[nx][ny]==max_num:
                # 행 먼저 -> 열
                if nx<max_r:
                    max_r=nx
                    max_c=ny
                if nx==max_r and ny<max_c:
                    max_c=ny
            # print(max_num, max_r,max_c)
            q.append((nx,ny))
    return max_r, max_c

ans_r, ans_c = r, c
for _ in range(k):
    max_r, max_c = bfs(ans_r,ans_c)
    if max_r ==1000 or max_c ==1000:
        break
    ans_r=max_r
    ans_c=max_c

print(ans_r+1,ans_c+1)