n, m, k = map(int,input().split())
apple_lst = []
for _ in range(m):
    apple_lst.append(tuple(map(int,input().split())))

def in_range(x,y):
    return 1<=x<=n and 1<=y<=n

d = dict()
d['U'] = (-1,0)
d['D'] = (1,0)
d['R'] = (0,1)
d['L'] = (0,-1)
# move
snake = [(1,1)]

def move():
    time = 0
    for _ in range(k):
        direction, distance = input().split()
        for _ in range(int(distance)):
            time+=1
            x, y = snake[-1]
            nx,ny = x+d[direction][0], y+d[direction][1]
            if not in_range(nx,ny): # 격자 밖으로 이동
                print(time)
                return
            if (nx,ny) in snake: # 겹쳤을 때
                print(time)
                return
            if (nx,ny) in apple_lst:
                snake.append((nx,ny))
            else:
                snake.append((nx,ny))
                snake.pop(0)
    else:
        print(time)
move()