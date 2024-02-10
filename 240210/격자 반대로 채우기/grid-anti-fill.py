n = int(input())
# 오른쪽 아래서부터 1부터 
# 위:행이 줄어드는 방향, 왼쪽, 아래: 행이 커지는 방향, 왼쪽: 열이 줄어드는 방향
dy, dx = [0,-1,0,-1], [-1,0,1,0]

graph = [[0]*n for _ in range(n)]
x,y = n-1, n-1
idx=0
# 행: x, 열: y
for num in range(1,n*n+1):
    graph[x][y]=num
    if num %n==0:
        idx= (idx+1)%4
    elif num!=1 and num%n==1:
        idx= (idx+1)%4
    x, y = x+dx[idx], y+dy[idx]

for x in range(n):
    for y in range(n):
        print(graph[x][y], end = ' ')
    print()