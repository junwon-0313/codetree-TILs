graph =[list(map(int, input().split())) for _ in range(4)]

ans = 0
for x in range(4):
    for y in range(4):
        if x>=y:
            ans += graph[x][y]
print(ans)