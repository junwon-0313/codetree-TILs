n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

ans =0
# 격자는 세로가 1이고 가로가 3이다.
for x in range(n):
    for y in range(n-2):
        total = graph[x][y]+graph[x][y+1]+graph[x][y+2]
        if total>ans:
            ans = total

print(ans)