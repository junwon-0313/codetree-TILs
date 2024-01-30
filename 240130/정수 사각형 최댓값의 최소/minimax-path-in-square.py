# 경로의 최댓값 중 최솟값
global N
N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

# 반드시 지나야하는 값이면 그 중에 최댓값
# 반드시 다른 경로가 있는 경우, 비교하여 최솟값
# 점화식: 위, 왼쪽 중 최솟값과 해당 위치에서의 최댓값
dp = [[0]*N for _ in range(N)]
def initialize():
    dp[0][0] = graph[0][0]
    for x in range(1,N):
        dp[x][0] = max(dp[x-1][0], graph[x][0])
    for y in range(1,N):
        dp[0][y] = max(dp[0][y-1], graph[0][y])

initialize()

for x in range(1,N):
    for y in range(1,N):
        dp[x][y]= max(min(dp[x-1][y], dp[x][y-1]), graph[x][y])

print(dp[N-1][N-1])