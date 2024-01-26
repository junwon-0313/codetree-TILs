n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 경로의 최대값-최소값의 최소값을 저장 
# dp = [[-1]*n for _ in range(n)]

# 오른쪽과 밑으로만 이동 가능
# 기존에 1 이 존재했으면 최솟값만 유지
# 기존과 차이가 적은 값을 유지

# 해당위치에서 최소, 최대값
cell1 = [[[]]*n for _ in range(n)]
cell2 = [[[]]*n for _ in range(n)]

def initialize():
    cell1[0][0] = [graph[0][0],graph[0][0]]
    cell2[0][0] = [graph[0][0],graph[0][0]]
    # dp[0][0]=0
    for x in range(1,n):
        cell1[x][0] = [min(graph[x][0], cell1[x-1][0][0]), max(graph[x][0], cell1[x-1][0][1])]
        cell2[x][0] = [min(graph[x][0], cell2[x-1][0][0]), max(graph[x][0], cell2[x-1][0][1])]
        # dp[x][0] = cell[x][0][1]-cell[x][0][0]
    for y in range(1, n):
        cell1[0][y] = [min(graph[0][y], cell1[0][y-1][0]), max(graph[0][y], cell1[0][y-1][1])]
        cell2[0][y] = [min(graph[0][y], cell2[0][y-1][0]), max(graph[0][y], cell2[0][y-1][1])]

        # dp[0][y] = cell[0][y][1]-cell[0][y][0]

initialize()
# print(cell)

for x in range(1,n):
    for y in range(1,n):
        # 위에서 아래로
        up_down = max(graph[x][y], cell1[x-1][y][1]) - min(graph[x][y], cell1[x-1][y][0])
        # 왼쪽에서 오른쪽으로 
        left_right = max(graph[x][y], cell1[x][y-1][1]) - min(graph[x][y], cell1[x][y-1][0])
        # x,y는 위와 왼쪽에서 올 수 있는데 기존 값과 비교해서 차이가 적은 값을 갱신
        # 같을 경우, 두개의 경우에 대해서 모두 살펴봐야함.
        if up_down >= left_right:
            cell1[x][y] = [min(graph[x][y], cell1[x][y-1][0]), max(graph[x][y], cell1[x][y-1][1])]
        else:
            cell1[x][y] = [min(graph[x][y], cell1[x-1][y][0]), max(graph[x][y], cell1[x-1][y][1])]

for x in range(1,n):
    for y in range(1,n):
        # 위에서 아래로
        up_down = max(graph[x][y], cell2[x-1][y][1]) - min(graph[x][y], cell2[x-1][y][0])
        # 왼쪽에서 오른쪽으로 
        left_right = max(graph[x][y], cell2[x][y-1][1]) - min(graph[x][y], cell2[x][y-1][0])
        # x,y는 위와 왼쪽에서 올 수 있는데 기존 값과 비교해서 차이가 적은 값을 갱신
        # 같을 경우, 두개의 경우에 대해서 모두 살펴봐야함.
        if up_down > left_right:
            cell2[x][y] = [min(graph[x][y], cell2[x][y-1][0]), max(graph[x][y], cell2[x][y-1][1])]
        else:
            cell2[x][y] = [min(graph[x][y], cell2[x-1][y][0]), max(graph[x][y], cell2[x-1][y][1])]

print(min(cell1[n-1][n-1][1]-cell1[n-1][n-1][0], cell2[n-1][n-1][1]-cell2[n-1][n-1][0]))

# for x in range(n):
#     for y in range(n):
#         print(cell1[x][y], end = ' ')
#     print()
# for x in range(n):
#     for y in range(n):
#         print(cell2[x][y], end = ' ')
#     print()