total = [] # 최종 초토화된 영역의 수를 저장
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

bomb_pos = [] # 폭탄 위치
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            bomb_pos.append((i,j))

# 출력 함수
def print_map(graph):
    for i in range(n):
        for j in range(n):
            print(graph[i][j], end =' ')
        print()

# 초토화된 영역의 개수 파악
def count(m):
    ans =0
    for i in range(n):
        for j in range(n):
            if m[i][j]==1:
                ans+=1
    return ans

def in_range(x,y):
    return 0<=x<n and 0<=y<n

# 행렬 복사함수
def copy(graph):
    new_graph = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_graph[i][j]=graph[i][j]
    return new_graph

# 첫번째 폭발
def bomb1(graph, x, y):
    dx, dy = [-2,-1,1,2],[0,0,0,0]
    for idx in range(4):
        nx, ny = x+dx[idx], y+dy[idx]
        if in_range(nx, ny) and graph[nx][ny]!=1:
            graph[nx][ny]=1
# # 두번째 폭발
def bomb2(graph, x, y):
    dx, dy = [-1,1,0,0],[0,0,-1,1]
    for idx in range(4):
        nx, ny = x+dx[idx], y+dy[idx]
        if in_range(nx, ny) and graph[nx][ny]!=1:
            graph[nx][ny]=1
# 세번째 폭발
def bomb3(graph, x, y):
    dx, dy = [-1,-1,1,1],[-1,1,-1,1]
    for idx in range(4):
        nx, ny = x+dx[idx], y+dy[idx]
        if in_range(nx, ny) and graph[nx][ny]!=1:
            graph[nx][ny]=1

# 재귀 함수
def bomb(graph, num):
    # 종료 조건: 폭탄이 모두 한번씩 터진 후
    if num == len(bomb_pos):
        total.append(count(graph))
        return
    x, y = bomb_pos[num]
    # 폭탄 터지는 방법 1
    new_graph = copy(graph) # 새로운 배열을 만들어서 전달
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