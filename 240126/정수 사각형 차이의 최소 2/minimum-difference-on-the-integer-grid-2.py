n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 경로의 최대값-최소값의 최소값을 저장 
# dp = [[-1]*n for _ in range(n)]

# 오른쪽과 밑으로만 이동 가능
# 기존에 1 이 존재했으면 최솟값만 유지
# 기존과 차이가 적은 값을 유지

# 해당위치에서 최소, 최대값
cell = [[[-1,-1]]*n for _ in range(n)]

def initialize():
    cell[0][0] = [graph[0][0],graph[0][0]]
    # dp[0][0]=0
    for x in range(1,n):
        cell[x][0] = [min(graph[x][0], cell[x-1][0][0]), max(graph[x][0], cell[x-1][0][1])]
        # dp[x][0] = cell[x][0][1]-cell[x][0][0]
    for y in range(1, n):
        cell[0][y] = [min(graph[0][y], cell[0][y-1][0]), max(graph[0][y], cell[0][y-1][1])]
        # dp[0][y] = cell[0][y][1]-cell[0][y][0]

initialize()
# print(cell)

for x in range(1,n):
    for y in range(1,n):
        # 위에서 아래로
        up_down = max(graph[x][y], cell[x-1][y][1]) - min(graph[x][y], cell[x-1][y][0])
        # 왼쪽에서 오른쪽으로 
        left_right = max(graph[x][y], cell[x][y-1][1]) - min(graph[x][y], cell[x][y-1][0])
        # x,y는 위와 왼쪽에서 올 수 있는데 기존 값과 비교해서 차이가 적은 값을 갱신
        if up_down > left_right:
            cell[x][y] = [min(graph[x][y], cell[x][y-1][0]), max(graph[x][y], cell[x][y-1][1])]
        else:
            cell[x][y] = [min(graph[x][y], cell[x-1][y][0]), max(graph[x][y], cell[x-1][y][1])]

print(cell[n-1][n-1][1]-cell[n-1][n-1][0])