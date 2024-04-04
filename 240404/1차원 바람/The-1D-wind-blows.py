n,m,q = map(int,input().split())
graph =[] # 전역 변수
for _ in range(n):
    graph.append(list(map(int,input().split())))
wind = []
for _ in range(q):
    r, d = input().split()
    wind.append((int(r)-1, d ))


def shift_right(lst): # 왼쪽에서 바람이 분 경우
    temp =lst.pop(-1)
    lst.insert(0,temp)
    return lst

def shift_left(lst):
    temp =lst.pop(0)
    lst.append(temp)
    return lst

def check(lst1, lst2):
    for idx in range(m):
        if lst1[idx]==lst2[idx]:
            return True
    return False

def check_up(raw, d): # option=1-> 위로, option =2 -> 아래로 
    q = [(raw,d)]
    while q:
        raw,d = q.pop()
        # 한칸 위가 존재하는지 범위 체크
        if raw-1<0:
            continue
        # 한칸 위랑 같은 칸이 존재하는지
        if check(graph[raw],graph[raw-1]):
            # 방향에 따라 반대로 밀고 
            if d =='R':
                graph[raw-1] = shift_right(graph[raw-1])
                q.append((raw-1,'L'))
            else:
                graph[raw-1] = shift_left(graph[raw-1])
                q.append((raw-1,'R'))

def check_down(raw, d): # option=1-> 위로, option =2 -> 아래로 
    q = [(raw,d)]
    while q:
        raw,d = q.pop()
        # 한칸 위가 존재하는지 범위 체크
        if raw+1>=n:
            continue
        # 한칸 위랑 같은 칸이 존재하는지
        if check(graph[raw],graph[raw+1]):
            # 방향에 따라 반대로 밀고 
            if d =='R':
                graph[raw+1] = shift_right(graph[raw+1])
                q.append((raw+1,'L'))
            else:
                graph[raw+1] = shift_left(graph[raw+1])
                q.append((raw+1,'R'))

def print_g():
    for x in range(n):
        for y in range(m):
            print(graph[x][y], end =' ')
        print()

for r, d in wind:
    # L은 왼쪽에서 R은 오른쪽에서 바람이 분다.
    # print('before')
    # print_g()
    # 방향으로 한칸 밈
    temp_raw = graph[r]
    if d =='L':
        graph[r] = shift_right(temp_raw)
    elif d =='R':
        graph[r] = shift_left(temp_raw)
    
    # 위로 # 숫자가 하나라도 겹치면 계속 진행
    check_up(r, d)
    # 아래로
    check_down(r, d)
# print('after')
print_g()