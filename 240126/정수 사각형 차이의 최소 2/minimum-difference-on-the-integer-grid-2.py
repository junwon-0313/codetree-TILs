# 주어진 숫자는 1에서 100까지임
# 최솟값이상의 수들로만 써서 이동한다는 가정하고 경로상의 수들 중 최댓값을 최소화하는 문제 
# 두번에 걸쳐서 풀이!
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def initialize(dp):
    global n
    dp[0][0]=graph[0][0]
    for x in range(1,n):
        dp[x][0] = max(dp[x-1][0], graph[x][0])
    for y in range(1,n):
        dp[0][y] = max(dp[0][y-1], graph[0][y])

score = []
for lower in range(1, 101):
    # 첫번째는 반드시 지나야하므로
    if lower > graph[0][0]:
        continue
    # 초기화
    dp = [[0]*n for _ in range(n)]
    initialize(dp)
    # 이동하면서 lower보다 큰 값 중만 통과하면서 가장 큰 수가 가장 작게
    for x in range(1,n):
        for y in range(1,n):
            if graph[x][y]>=lower and dp[x-1][y]!=0 and dp[x][y-1]!=0:
                dp[x][y] = max(min(dp[x-1][y], dp[x][y-1]), graph[x][y])
            elif graph[x][y]>=lower and dp[x-1][y]!=0:
                dp[x][y] = max(dp[x-1][y], graph[x][y])
            elif graph[x][y]>=lower and dp[x][y-1]!=0:
                dp[x][y] = max(dp[x][y-1], graph[x][y])


    if dp[n-1][n-1]==0:
        pass
    else:
        score.append(dp[n-1][n-1]-lower)
# print(score)
print(min(score))