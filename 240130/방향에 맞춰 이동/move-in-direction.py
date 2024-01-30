N = int(input())
# 서 남 북 동
# W S N E
dx, dy = [-1,0,0,1], [0,-1,1,0]
lst = [list(input().split()) for _ in range(N)]

x,y = 0, 0
for direction, distance in lst:
    distance = int(distance)
    if direction=='W':
        x += dx[0]*distance
        y += dy[0]*distance
    elif direction=='S':
        x += dx[1]*distance
        y += dy[1]*distance
    elif direction=='N':
        x += dx[2]*distance
        y += dy[2]*distance
    elif direction=='E':
        x += dx[3]*distance
        y += dy[3]*distance
print(x,y)