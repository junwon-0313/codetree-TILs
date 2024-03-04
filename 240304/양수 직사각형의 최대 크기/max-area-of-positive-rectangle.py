# 가능한 양수 직사각형 중 최대 크기
# 방향은 오른쪽 아래로만 가도 충분함, 중복됨
# 시간 복잡도: O(n*m*n*m)
n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
ans = -1
def rectangle(x,y): #x,y에서 n,m까지 진행
    global ans
    lst = []
    for nx in range(x,n):
        cnt = 0
        for ny in range(y, m):
            if graph[nx][ny]>0:
                cnt+=1
            else:
                break
        lst.append(cnt)
    
    min_rect = 100
    for idx, s in enumerate(lst):
        min_rect= min(min_rect,s)
        rect_size = min_rect*(idx+1)
        if ans<rect_size:
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