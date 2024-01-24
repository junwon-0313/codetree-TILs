# 이동한 경로의 최솟값이 최대가 되는 경로
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

dp = [[0]*N for _ in range(N)]

# 초기 설정
def initialize():
    global N
    dp[0][0] = graph[0][0]
    for i in range(1,N):
        dp[0][i] = min(dp[0][i-1], graph[0][i])
        dp[i][0] = min(dp[i-1][0], graph[i][0])
initialize()

# 위에서 아래로, 좌에서 우로
# 반드시 지나야하는 경로만 최소값으로 변경, 왼, 위 중에 큰 값과 해당 위치 값 중 최소값을 사용
for x in range(1,N):
    for y in range(1,N):
        dp[x][y] = min(graph[x][y], max(dp[x-1][y], dp[x][y-1]))

# # dp 출력
# for x in range(N):
#     for y in range(N):
#         print(dp[x][y],end = ' ')
#     print()
print(dp[N-1][N-1])