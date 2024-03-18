n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

def in_range(x,y):
    return 0<=x<n and 0<=y<n

# 폭탄을 터트림
# def bomb(x,y):
#     num= graph[x][y]-1
#     for nx in range(x-num,x+num+1): # 열
#         if in_range(nx,y):
#             graph[nx][y]=-1
#     for ny in range(y-num,y+num+1): # 행
#         if in_range(x,ny):
#             graph[x][ny]=-1
def bomb_gravity(x,y,graph):
    num= graph[x][y]-1
    y_cnt = 0
    for nx in range(x-num,x+num+1): # 열
        if in_range(nx,y):
            graph[nx][y]=-1
            y_cnt+=1
    for ny in range(y-num,y+num+1): # 행
        if ny==y:
            continue
        if in_range(x,ny):
            for nx in range(1,x):
                graph[nx][ny] = graph[nx-1][ny]
            graph[0][ny]=-1
    # y에서 하나는 반드시 터짐 -> 여기를 보완 
    for nx in range(n):
        if graph[nx][y]==-1:
            break
        graph[nx+y_cnt-1][y] = graph[nx][y]
        graph[nx][y]=-1
    return graph


def print_graph(graph):
    for x in range(n):
        for y in range(n):
            print(graph[x][y], end = ' ')
        print()

# 방향 존재, 방문처리 
dxs,dys = [1,0], [0,1]
def find_couple(graph):
    cnt = 0
    for x in range(n):
        for y in range(n):
            if graph[x][y]==-1:
                continue
            for dx, dy in zip(dxs, dys):
                nx, ny= x+dx, y+dy
                if in_range(nx,ny) and graph[x][y] == graph[nx][ny]:
                    cnt+=1
    return cnt

def copy_graph(graph):
    tmp_graph=[]
    for i in range(n):
        tmp_graph.append(graph[i][:])
    return tmp_graph

max_ans =-1
for x in range(n):
    for y in range(n):
        tmp_graph = copy_graph(graph)
        # print('INIT')
        # print_graph(tmp_graph)
        bomb_gravity(x,y,tmp_graph)
        # print('AFTER BoMB')
        # print_graph(tmp_graph)
        tmp_cnt = find_couple(tmp_graph)
        if tmp_cnt>max_ans:
            max_ans=tmp_cnt
print(max_ans)