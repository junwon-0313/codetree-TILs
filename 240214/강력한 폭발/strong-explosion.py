# 초토화시키는 지역의 최대화
total = []
# 폭탄 10개
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 폭탄 위치
bomb_pos = []
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            bomb_pos.append((i,j))

def print_map(graph):
    for i in range(n):
        for j in range(n):
            print(graph[i][j], end =' ')
        print()

def count(m):
    ans =0
    for i in range(n):
        for j in range(n):
            if m[i][j]==0:
                ans+=1
    return n**2-ans

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def copy(graph):
    new_graph = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_graph[i][j]=graph[i][j]
    return new_graph

def bomb1(graph, x, y):
    dx, dy = [-2,-1,1,2],[0,0,0,0]
    for idx in range(n):
        nx, ny = x+dx[idx], y+dy[idx]
        if in_range(nx, ny) and graph[nx][ny]!=1:
            graph[nx][ny]=2
def bomb2(graph, x, y):
    dx, dy = [-1,1,0,0],[0,0,-1,1]
    for idx in range(n):
        nx, ny = x+dx[idx], y+dy[idx]
        if in_range(nx, ny) and graph[nx][ny]!=1:
            graph[nx][ny]=2

def bomb3(graph, x, y):
    dx, dy = [-1,-1,1,1],[-1,1,1,-1]
    for idx in range(n):
        nx, ny = x+dx[idx], y+dy[idx]
        if in_range(nx, ny) and graph[nx][ny]!=1:
            graph[nx][ny]=2

# 재귀 함수
# x,y 위치에서 폭탄 터트리기
def bomb(graph, num):
    # print('@@', num)
    # print_map(graph)
    # 종료 조건
    if num == len(bomb_pos):
        total.append(count(graph))
        return
    x, y = bomb_pos[num]
    # 폭탄 터지는 방법 1
    # 새로운 배열을 만들어서 전달
    new_graph = copy(graph)
    bomb1(new_graph,x,y)
    bomb(new_graph,num+1)
    # 폭탄 터지는 방법 2
    new_graph = copy(graph)
    bomb2(new_graph,x,y)
    bomb(new_graph,num+1)

    # 폭탄 터지는 방법 3
    new_graph = copy(graph)
    bomb3(new_graph,x,y)
    bomb(new_graph,num+1)

bomb(graph, 0)
print(max(total))