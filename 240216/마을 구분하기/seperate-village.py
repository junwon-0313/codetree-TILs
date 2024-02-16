# 마을의 개수, 마을 사람 수, 정렬 후 출력
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
dxs, dys = [0,0,1,-1], [1,-1,0,0]
town_lst = []

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def make_group(x,y):
    global people
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if not in_range(nx,ny) or visited[nx][ny] or graph[nx][ny]==0:
            continue
        visited[nx][ny]=True
        people+=1
        make_group(nx,ny)

        

# 모든 시작점에서
for x in range(n):
    for y in range(n):
        if graph[x][y]==0:
            continue
        if not visited[x][y]:
            visited[x][y]=True
            people =1
            make_group(x,y)
            town_lst.append(people)

print(len(town_lst))
town_lst.sort()
for num in town_lst:
    print(num)