n,m,t = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
ball =[]
for _ in range(m):
    ball.append(tuple(map(int, input().split())))

def in_range(x,y):
    return 0<=x<n and 0<=y<n
dxs, dys= (-1,1,0,0), (0,0,-1,1)

def move(x,y):
    tmp_lst =[]
    idx =0
    for dx, dy in zip(dxs,dys):
        nx,ny = x+dx,y+dy
        if not in_range(nx,ny):
            idx+=1
            continue
        # if graph[nx][ny]>graph[x][y]:
        tmp_lst.append((graph[nx][ny],idx))
        idx+=1
    tmp_lst.sort(key=lambda x: (-x[0], x[1]))
    move_dir = tmp_lst[0][1]
    return move_dir

        
for time in range(t):
    new_ball =[]
    for x,y in ball:
        x, y = x-1, y-1
        move_dir = move(x,y)
        new_ball.append((x+dxs[move_dir], y+dys[move_dir]))
    ball =[]
    for x, y in new_ball:
        if new_ball.count((x,y))==1:
            ball.append((x,y))

print(len(ball))