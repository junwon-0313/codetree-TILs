# 편안한 상태: 방금 칠해진 칸을 기준으로 인접 4칸 중 3개가 색칠
N, M = map(int, input().split())
lst = [list(map(int,input().split())) for _ in range(M)]
painted = [[False]*(N+1) for _ in range(N+1)]
dx, dy = [0,0,1,-1], [1,-1,0,0]
for x,y in lst:
    painted[x][y]=True
    cnt = 0
    for idx in range(4):
        nx, ny = x+dx[idx], y+dy[idx]
        if 1<=nx<=N and 1<=ny<=N:
            if painted[nx][ny]:
                cnt+=1
    if cnt==3:
        print(1)
    else:
        print(0)