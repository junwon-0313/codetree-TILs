global N
N = int(input())
graph = [list(input()) for _ in range(N)]
K = int(input())
# 아, 오, 위, 왼 
dx, dy = [1,0,-1,0], [0,1,0,-1]
if K<=N:
    x,y = 0, K-1
    di= 0 
elif N<K<=2*N:
    x,y = K%N-1, N-1
    di =3
elif 2*N<K<=3*N:
    x, y = N-1, N-1-(K%N)+1
    di = 2
else:
    x, y =  N-1-(K%N)+1, 0
    di =1

def in_range(x, y):
    return 0<=x<N and 0<=y<N

cnt = 0
while True:
    # 거울에 부딪힘
    cnt+=1
    if graph[x][y]=='/':
        if di ==0:
            di=3
        elif di==1:
            di=2
        elif di==2:
            di=1
        elif di==3:
            di=0

    elif graph[x][y]=='\\':
        if di ==0:
            di=1
        elif di==1:
            di=0
        elif di==2:
            di=3
        elif di==3:
            di=2
    nx, ny = x+dx[di], y+dy[di]
    if not in_range(nx,ny):
        print(cnt)
        break
    x,y = nx, ny