# Memoization
# x,y에서 출발하여 조건을 만족하며 도달할 수 있는 칸의 수 중 최대 칸의 수
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1]*n for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

# 피보나치 수열과 비슷
# x,y에서 시작해서 얼마나 많이 갈 수 있는지
def find_max(x,y):
    # 이미 값이 있다면 바로 반환
    if dp[x][y] !=-1:
        return dp[x][y]

    best = 1
    dxs, dys = [-1,1,0,0], [0,0,1,-1]

    # 4 방향을 살펴보며 최적의 칸 수를 계산
    for dx,dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        # 이동했다 -> 이전에 이동한 값에서의 최대값 +1, 이동이 없다면 best=1
        if in_range(nx,ny) and graph[nx][ny]>graph[x][y]:
            best = max(best, find_max(nx,ny) +1)
    dp[x][y] = best
    return dp[x][y]

ans =0
for i in range(n):
    for j in range(n):
        ans = max(ans, find_max(i,j))
print(ans)