n, m = map(int,input().split())
graph = [[0]*n for _ in range(n)]
for _ in range(m):
    x, y = map(int,input().split())
    graph[x-1][y-1] = x*y

for x in range(n):
    for y in range(n):
        print(graph[x][y], end = ' ')
    print()