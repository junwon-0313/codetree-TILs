r, c = map(int,input().split())
graph = []
for _ in range(r):
    graph.append(list(input().split()))

ans =0
# 점프는 오른쪽 아래로만 진행
if graph[0][0]!=graph[r-1][c-1]:
    for x1 in range(1,r-1):
        for y1 in range(1,c-1):
            for x2 in range(1,r-1):
                for y2 in range(1,c-1):
                    # 두 점만 경유하여 도착
                    if graph[x1][y1] != graph[0][0] and graph[x2][y2] != graph[r-1][c-1] and x1<x2 and y1<y2:
                        ans+=1
print(ans)