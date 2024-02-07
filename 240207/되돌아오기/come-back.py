N = int(input())
move_lst = [list(input().split()) for _ in range(N)]

x, y = 0, 0
#  동 서 남 북
direction = dict()
direction['E'] = [1,0]
direction['W'] = [-1,0]
direction['S'] = [0,1]
direction['N'] = [0,-1]
cnt = 0
for di, dis in move_lst:
    for _ in range(int(dis)):
        cnt +=1
        x, y = x+direction[di][0], y+direction[di][1]
        if x==0 and y==0:
            print(cnt)
            cnt =-1
            break
    if cnt==-1:
        break

if (x,y)!=(0,0):
    print(-1)