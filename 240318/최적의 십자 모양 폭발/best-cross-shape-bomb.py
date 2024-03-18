n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

# 범위 체크
def in_range(x,y):
    return 0<=x<n and 0<=y<n

# 폭탄
def bomb(x,y,graph):
    num= graph[x][y]-1
    for nx in range(x-num,x+num+1): # 열
        if in_range(nx,y):
            graph[nx][y]=-1
    for ny in range(y-num,y+num+1): # 행
        if in_range(x,ny):
            graph[x][ny]=-1
    return graph, num

# 중력 
def gravity(graph, num):
    for ny in range(y-num,y+num+1):
        if in_range(x,ny):
            # y에서 하나는 반드시 터짐 -> 여기를 보완
            num_lst= []
            y_cnt = 0
            for nx in range(n):
                if graph[nx][ny]==-1:
                    y_cnt+=1
            for nx in range(n):
                if graph[nx][ny]==-1:
                    break
                num_lst.append(graph[nx][ny])
            for nx in range(n):
                if nx+1 <=y_cnt:
                    graph[nx][ny]=-1
                else:
                    break
            for idx in range(len(num_lst)):
                graph[y_cnt+idx][ny]=num_lst[idx]
    return graph

# 출력 함수
def print_graph(graph):
    for x in range(n):
        for y in range(n):
            print(graph[x][y], end = ' ')
        print()

# 오른쪽과 아래 방향만 탐색
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

max_ans =-1
for x in range(n):
    for y in range(n):
        tmp_graph = [i[:] for i in graph] # copy
        tmp_graph,num = bomb(x,y,tmp_graph)
        tmp_graph = gravity(tmp_graph, num)
        # print_graph(tmp_graph) # 출력
        tmp_cnt = find_couple(tmp_graph)
        if tmp_cnt>max_ans:
            max_ans=tmp_cnt
print(max_ans)