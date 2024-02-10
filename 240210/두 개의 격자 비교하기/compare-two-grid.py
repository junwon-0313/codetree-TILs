n,m = map(int, input().split())
graph1, graph2 = [], []
for _ in range(n):
    graph1.append(list(map(int, input().split())))

for _ in range(n):
    graph2.append(list(map(int, input().split())))

for x in range(n):
    for y in range(m):
        if graph1[x][y]==graph2[x][y]:
            print(0, end = ' ')
        else:
            print(1, end = ' ')
    print()