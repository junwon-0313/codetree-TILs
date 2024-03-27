n, m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

def in_range(x,y):
    return 0<=x<n and 0<=y<m

blocks = [[(0,0),(0,1),(1,0)],[(0,0),(0,1),(1,1)],[(0,0),(1,1),(1,0)],[(1,1),(0,1),(1,0)],[(0,0),(0,1),(0,2)],[(0,0),(1,0),(2,0)]]

max_val = 0
for x in range(n):
    for y in range(m):
        # x,y 기준으로 여러 모양 블럭을 진행
        for block in blocks:
            cnt =0
            for dx,dy in block:
                nx, ny = x+dx, y+dy
                if not in_range(nx,ny):
                    cnt=0
                    break
                cnt+=graph[nx][ny]
            max_val = max(max_val, cnt)

print(max_val)