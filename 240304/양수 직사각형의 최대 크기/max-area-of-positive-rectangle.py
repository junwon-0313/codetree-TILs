# 가능한 양수 직사각형 중 최대 크기
# 방향은 오른쪽 아래로만 가도 충분함, 중복됨
# 시간 복잡도: O(n*m*n*m)
n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
ans = -1
def rectangle(x,y): #(x,y)에서 (n,m)까지 탐색
    global ans
    lst = [] # (x,y)를 시작하여 각 행에서 만들 수 있는 직사각형의 크기를 저장
    for nx in range(x,n):
        cnt = 0
        for ny in range(y, m):
            if graph[nx][ny]>0:
                cnt+=1
            else:
                break
        lst.append(cnt) 
    min_rect = 100 # 최댓값으로 초기화
    for idx, s in enumerate(lst):
        min_rect= min(min_rect,s) # 한 점을 시작으로 직사각형이 되려면 해당 조건을 따라야 함.
        rect_size = min_rect*(idx+1) # 세로 x 가로
        if ans<rect_size: # 최댓값 업데이트
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