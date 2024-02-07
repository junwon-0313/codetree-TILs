x, y = 0, 0
di = 0
lst = input()
# L,R 방향 전환
dx, dy = [0, 1, 0, -1], [-1,0,1, 0]
cnt = 0
for c in lst:
    cnt +=1
    if c=='L':
        di= (di-1)%4
    elif c=='R':
        di= (di+1)%4
    elif c=='F':
        x, y = x+ dx[di], y+dy[di]
        if x ==0 and y==0:
            print(cnt)
            break
else:
    print(-1)