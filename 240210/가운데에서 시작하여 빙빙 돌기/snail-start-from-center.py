n = int(input())
x, y = n//2, n//2
# 오, 위, 왼, 아
dx, dy = [0,-1,0,1],[1,0,-1,0]
# 1 1 2 2 3 3 4 4
cnt = []
for i in range(1,n+1):
    cnt.append(i)
    cnt.append(i)

num,idx =1, 0
graph=[[0]*n for _ in range(n)]
# 초기값
graph[x][y]=num
for i in cnt:
    for j in range(i):
        num+=1
        # 이동 후
        x, y = x+dx[idx], y+dy[idx]
        # 범위를 넘어가면 종료
        if x<0 or x>=n or y<0 or y>=n:
            break
        # 값을 넣어주기
        graph[x][y]=num
    idx= (idx+1)%4

for x in range(n):
    for y in range(n):
        print(graph[x][y], end = ' ')
    print()