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
    # 몇번째 행 열까지 진행해도 되는지 체크
    end_x, end_y = n,m
    for nx in range(x, n):
        if graph[nx][y]<=0:
            end_x=nx
            break
    for ny in range(y,m):
        if graph[x][ny]<=0:
            end_y=ny
            break

    for nx in range(x,end_x): # 행을 고정
        for ny in range(y,end_y):
            if graph[nx][ny]<=0:
                return # 종료
        rect_size = (nx-x+1)*(ny-y+1)
        # print('행 고정',rect_size, nx,x,ny,y)
        if rect_size>ans:
            ans = rect_size
    
    for ny in range(y,end_y): # 열을 고정
        for nx in range(x,end_x): 
            if graph[nx][ny]<=0:
                return # 종료
        rect_size = (nx-x+1)*(ny-y+1)
        # print('열 고정',rect_size)
        if rect_size>ans:
            ans = rect_size

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