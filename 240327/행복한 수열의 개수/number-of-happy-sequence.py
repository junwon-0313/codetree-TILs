n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

ans =0
# 행 마다
for x in range(n):
    max_cnt =1
    cnt = 1
    pre = graph[x][0]
    for y in range(1,n):
        if pre ==graph[x][y]:
            cnt+=1
        else:
            pre = graph[x][y]
            cnt=1
        max_cnt = max(max_cnt, cnt)
    if max_cnt>=m:
        ans+=1
# 열마다
for y in range(n):
    max_cnt =1
    cnt = 1
    pre = graph[0][y]
    for x in range(1,n):
        if pre ==graph[x][y]:
            cnt+=1
        else:
            pre = graph[x][y]
            cnt=1
        max_cnt = max(max_cnt, cnt)
    if max_cnt>=m:
        ans+=1
print(ans)