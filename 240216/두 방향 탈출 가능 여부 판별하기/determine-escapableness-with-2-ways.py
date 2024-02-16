# 그리드 상에서의 DFS 탐색
# 아래 -> 오른쪽
# x,y: 행, 열
# 이동, 방문체크 -> 격자안, 방문x, 조건: 뱀
# 재귀 함수 호출 전에 방문처리!! -> 여기서는 방문처리 안해도됨
n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dxs, dys = [1,0], [0,1]

def in_range(x,y):
    return 0<=x<n and 0<=y<m


Final = False
def dfs(x,y):
    global Final
    if x==n-1 and y==m-1:
        Final= True
        return 
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if not in_range(nx,ny): # 범위 체크
            continue
        if graph[nx][ny]==0: # 뱀 만남
            continue
        dfs(nx,ny)

dfs(0,0)
if Final:
    print(1)
else:
    print(0)