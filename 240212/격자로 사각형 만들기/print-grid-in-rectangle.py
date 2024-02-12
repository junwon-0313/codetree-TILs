n = int(input())
graph = [[0]*n for _ in range(n)]
def initialize():
    for x in range(n):
        graph[x][0]=1
        graph[0][x]=1

initialize()
for x in range(1,n):
    for y in range(1,n):
        graph[x][y]= graph[x-1][y]+ graph[x][y-1] + graph[x-1][y-1]


for x in range(n):
    for y in range(n):
        print(graph[x][y],end=' ')
    print()