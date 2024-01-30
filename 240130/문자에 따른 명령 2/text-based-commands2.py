# L: 반시계, R: 시계
# 동 남 서 북
dx, dy = [1,0,-1,0], [0,-1,0,1]
lst = list(input())

x,y, dir_num = 0, 0, 3
for i in lst:
    if i =='R':
        dir_num = (dir_num+1)%4

    elif i=='L':
        dir_num = (dir_num-1)%4

    elif i =='F':
        x, y = x+dx[dir_num], y+dy[dir_num]
        
print(x,y)