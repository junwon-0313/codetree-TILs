n = int(input())
graph =[]
for _ in range(n):
    graph.append(list(map(int,input().split())))
max_coin=0
for x in range(n-2):
    for y in range(n-2):
        coin =0
        for nx in range(x,x+3):
            for ny in range(y,y+3):
                if graph[nx][ny]:
                    coin+=1
        max_coin = max(coin, max_coin)
print(max_coin)