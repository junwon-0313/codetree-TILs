n,t = map(int, input().split())
x,y, idx =n//2, n//2, 0
# 북 동 남 서 
dx, dy =[-1,0,1,0],[0,1,0,-1]
command = list(input())
graph =[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

def in_range(x,y):
    return 0<=x<n and 0<=y<n

answer = graph[x][y]
for cmd in command:
    if cmd=='L':
        idx= (idx-1)%4
    elif cmd =='R':
        idx = (idx+1)%4
    else:
        nx, ny = x+dx[idx], y+dy[idx]
        if in_range(nx, ny):
            x,y= nx, ny
            answer+=graph[nx][ny]
print(answer)