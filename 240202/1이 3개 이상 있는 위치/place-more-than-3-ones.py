global n
n = int(input())
graph =[list(map(int,input().split())) for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

dx, dy = [1,-1,0,0], [0,0,1,-1]
total = 0
for x in range(n):
    for y in range(n):
        tmp = 0
        for idx in range(4):
            nx,ny = x+dx[idx], y+dy[idx]
            if in_range(nx,ny) and graph[nx][ny]==1:
                tmp+=1
        if tmp>=3:
            total+=1
print(total)