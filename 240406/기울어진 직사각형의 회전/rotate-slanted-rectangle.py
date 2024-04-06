n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
r, c, m1, m2, m3, m4, d = map(int,input().split())

def print_g():
    for x in range(n):
        for y in range(n):
            print(graph[x][y], end = ' ')
        print()



def rotate_g(x,y, k, l, d):
    temp_g = [[-1]*n for _ in range(n)]
    if d ==0: 
        dxs, dys = [-1,-1,1,1], [1,-1,-1,1]
        move_nums = [k,l,k,l]
    else:
        dxs, dys = [-1,-1,1,1], [-1,1,1,-1]
        move_nums = [l,k,l,k]

    for dx, dy, move_num in zip(dxs, dys, move_nums):
        for _ in range(move_num):
            nx, ny = x+dx, y+dy
            temp_g[nx][ny] = graph[x][y]
            x, y = nx,ny
    for i in range(n):
        for j in range(n):
            if temp_g[i][j]==-1:
                continue
            graph[i][j] = temp_g[i][j]


rotate_g(r-1,c-1,m1,m2,d)
print_g()