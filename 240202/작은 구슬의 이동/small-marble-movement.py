global n
n, t = map(int, input().split())

r, c, d = list(input().split())

if d=='U':
    idx= 0
elif d=='D':
    idx=3
elif d=='L':
    idx=1
elif d =='R':
    idx=2

# 상 좌 우 하
dx, dy = [0,-1,1,0], [-1,0,0,1]
def in_range(x,y):
    return 0<=x<n and 0<=y<n

x,y = int(r)-1, int(c)-1
for i in range(t):
    nx,ny = x+dx[idx], y+dy[idx]
    if in_range(nx,ny):
        x,y = nx,ny
    else:
        idx = 3-idx
print(x, y)