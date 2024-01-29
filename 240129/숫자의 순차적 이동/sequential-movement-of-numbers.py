n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

num_pos = [[] for _ in range(n*n+1)]
def find_pos():
    for x in range(n):
        for y in range(n):
            num_pos[graph[x][y]] = (x,y)
find_pos()

dx, dy = [1,1,-1,-1,0,0,1,-1], [1,-1,1,-1,-1,1,0,0]
# 총 m 번 반복
for _ in range(m):
    # 1번부터 n^2까지 순서대로 조건에 따라 변경
    for i in range(1, n**2+1):
        x, y = num_pos[i]
        find_max = []
        # 8개 방향 중에서 max 값을 찾은 후, 위치 변경
        for idx in range(8):
            nx,ny = x+dx[idx], y+dy[idx]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            find_max.append(graph[nx][ny])
        max_num = max(find_max)
        max_x, max_y = num_pos[max_num]
        # 위치와 그래프에서의 값 갱신
        num_pos[max_num],num_pos[i] = (x,y), (max_x, max_y)
        graph[x][y], graph[max_x][max_y] = graph[max_x][max_y], graph[x][y]

# 출력
for x in range(n):
    for y in range(n):
        print(graph[x][y], end = ' ')
    print()