# 가능한 양수 직사각형 중 최대 크기
# 한 점을 포함하는 가능한 직사각형을 모두 구한다.
n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
ans = -1
# 방향은 오른쪽 아래로만 가도 충분함, 중복됨
# 시간 복잡도: O(n*m*n*m)
# def in_range(x,y):
#     return 0<=x<n and 0<=y<m
def rectangle(x,y):
    global ans
    for nx in range(x,n): # 행을 고정
        for ny in range(y,m):
            if graph[nx][ny]<0:
                return # 종료
        rect_size = (nx-x+1)*(ny-y+1)
        if rect_size>ans:
            ans = rect_size
    
    for ny in range(y,m): # 열을 고정
        for nx in range(x,n): 
            if graph[nx][ny]<0:
                return # 종료
        rect_size = (nx-x+1)*(ny-y+1)
        if rect_size>ans:
            ans = rect_size

dxs, dys =[1,0],[0,1]
# 시작점: 양수
for x in range(n):
    for y in range(m):
        # 방문처리는 따로 필요없음: 방향이 정해짐
        if graph[x][y]>0:
            rectangle(x,y)

if ans==-1:
    print(-1)
else:
    print(ans)