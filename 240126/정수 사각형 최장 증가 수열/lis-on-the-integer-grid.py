# 각 칸에 적혀있는 수가 증가하는 순서대로 진행해야한다 -> 조건
# 각 칸에 적혀있는 수들 중에서 작은값부터 순서대로 dp 값을 갱신
# 칸에 적혀있는 수가 작은 것부터 오름차순 정렬하여 순서대로 dp값을 갱신!
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

pos = []
# dp를 1로 초기화: 하나는 무조건 존재
dp = [[1]*n for _ in range(n)]

# 그래프 안의 값으로 오름차순 정렬을 하기 위해서 
for x in range(n):
    for y in range(n):
        # 값, 행, 열
        pos.append((graph[x][y], x, y))

pos.sort()

dx, dy = [0,0,1,-1], [1,-1,0,0]

for num, x, y in pos:
    for idx in range(4):
        nx, ny = x+dx[idx], y+dy[idx]
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        if graph[nx][ny]>num:
            dp[nx][ny]+=1

def find_max(dp):
    global n
    max_num = 0
    for x in range(n):
        for y in range(n):
            if dp[x][y] > max_num:
                max_num = dp[x][y]
    return max_num

print(find_max(dp))