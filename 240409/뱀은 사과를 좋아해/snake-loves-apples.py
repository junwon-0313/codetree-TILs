n, m, k = map(int,input().split())
apple_lst = []
for _ in range(m):
    apple_lst.append(tuple(map(int,input().split())))

def in_range(x,y):
    return 1<=x<=n and 1<=y<=n

d = dict()
d['U'] = (-1,0)
d['D'] = (1,0)
d['R'] = (0,1)
d['L'] = (0,-1)
# -1은 뱀이 존재, 1은 사과 존재
graph = [[0]*(n+1) for _ in range(n+1)]
graph[1][1]=-1

move_lst = [] 
for _ in range(k):
    direction, distance = input().split()
    move_lst.append((direction,distance))

# 사과 위치 표시, 한 번 먹으면 뱀으로 변경
for x,y in apple_lst:
    graph[x][y]=1

def move():
    # 뱀 위치 표현
    head_pos = (1,1)
    tail_pos = [(1,1)]
    time=0
    for direction, distance in move_lst:
        for _ in range(int(distance)):
            time+=1
            x,y = head_pos
            nx, ny = x+ d[direction][0], y+ d[direction][1]
            if not in_range(nx,ny):
                print(time)
                return
            if graph[nx][ny]==-1:
                print(time)
                return
            if graph[nx][ny]==0:
                tail_x,tail_y = tail_pos.pop(0)
                graph[tail_x][tail_y]=0

            head_pos = (nx,ny)
            tail_pos.append((nx,ny))
            graph[nx][ny]=-1
            # 사과가 있을 때 -> 꼬리 +1
    else:
        print(time)
move()