n = int(input())
# 왼 위 오 아
dx, dy = [0,-1,0,1],[-1,0,1,0]
num,idx =n*n, 0
x, y = n-1,n-1
graph=[[0]*n for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

while True:
    if num==0:
        break
    # 값을 할당
    graph[x][y]= num
    num-=1
    nx, ny = x+dx[idx], y+dy[idx]
    if in_range(nx,ny) and graph[nx][ny]==0:
        x,y= nx,ny
    else:
        idx= (idx+1)%4
        x, y = x+dx[idx], y+dy[idx]

for x in range(n):
    for y in range(n):
        print(graph[x][y], end = ' ')
    print()