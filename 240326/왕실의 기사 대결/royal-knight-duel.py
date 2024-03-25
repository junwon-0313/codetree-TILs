l, n, q = map(int, input().split())
graph = []
for _ in range(l):
    graph.append(list(map(int,input().split())))
knight = [] # 0번부터 ~
heal = [] # 초기 체력 저장
for _ in range(n):
    r,c,h,w,k = map(int,input().split())
    knight.append([r-1,c-1,h,w,k])
    heal.append(k)

# 위 오 아 왼
dxs, dys = [-1,0,1,0], [0,1,0,-1]

def in_range(x,y):
    return 0<=x<l and 0<=y<l

def search_place(r,c,h,w,d):
    tmp_lst = []
    if d==0:
        for i in range(w):
            tmp_lst.append((r-1,c+i))
    elif d==1:
        for i in range(h):
            tmp_lst.append((r+i,c+w))
    elif d==2:
        for i in range(w):
            tmp_lst.append((r+h,c+i))
    elif d==3:
        for i in range(h):
            tmp_lst.append((r+i,c-1))
    return tmp_lst

def knight_exist(x,y,num,meet_lst):
    for idx in range(n):
        if num==idx:
            continue
        if died[idx]:
            continue
        r,c,h,w,k = knight[idx]
        for i in range(h):
            for j in range(w):
                if (r+i,c+j) == (x,y) and idx not in meet_lst:
                    meet_lst.append(idx)
                    break
    return meet_lst

def bfs_move(i, d):
    q = [i]
    move_knight=[] # 밀쳐진 기사 리스트 

    while q:
        knight_num = q.pop(0)
        move_knight.append(knight_num)
        r,c,h,w,k = knight[knight_num]
        # d방향으로 한칸 갈 때, 확인해야되는 영역을 구한다. 
        search_lst = search_place(r,c,h,w,d)

        meet_lst =[]
        for nx,ny in search_lst:
            # 벽을 만날 경우 바로 종료
            if not in_range(nx,ny):
                return []
            if graph[nx][ny]==2:
                return []
            meet_lst = knight_exist(nx,ny,knight_num, meet_lst)

        for idx in meet_lst:
            q.append(idx)
    return move_knight

def damage(move_lst, d):
    for idx, num in enumerate(move_lst):
        r,c,h,w,k = knight[num]
        # 좌표 이동
        r, c = r+dxs[d], c+dys[d]
        if idx==0:
            knight[num] = [r,c,h,w,k]
        else:
            demage = 0
            for i in range(h):
                for j in range(w):
                    if graph[r+i][c+j]==1:
                        demage+=1
            k -=demage
            if k<=0: # 체력이 마이너스인 경우, 죽음 처리
                died[num]=True
            else:
                knight[num] = [r,c,h,w,k]

# 명령 실행
died = [False for _ in range(n)]
for _ in range(q):
    i,d = map(int,input().split())
    if died[i-1]: # 죽었으면 skip
        continue
    # 이동
    move_knight = bfs_move(i-1, d)
    # print(move_knight)

    # 데미지
    damage(move_knight, d)
    # print('기사\n', knight)
    # print('생존여부\n', died)

# 생존 기사들이 받은 데미지의 합을 출력
total_damage = 0
for num in range(n):
    if died[num]:
        continue
    total_damage+=(heal[num]-knight[num][4])
print(total_damage)