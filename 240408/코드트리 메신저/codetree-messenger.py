n, q = map(int,input().split())

class Query:
    def __init__(self, cmd, other):
        self.cmd = cmd
        self.other = other

q_lst = []
for _ in range(q):
    temp_lst = list(map(int,input().split()))
    q_lst.append(Query(temp_lst[0], temp_lst[1:]))

parent = [-1 for _ in range(n+1)]
authority = [-1 for _ in range(n+1)]
alarm = [True for _ in range(n+1)] # 켜져있음 T

def find_chat(c):
    # 한 부모의 자식은 다른 부모의 자식일 수 없으므로 방문 처리 필요없음
    tree = dict()
    for idx, p in enumerate(parent):
        if idx ==0:
            continue
        if p in tree:
            tree[p].append(idx)
        else:
            tree[p] = [idx]
    # print(tree)
    cnt = 0
    child_lst = [(c,0)]
    while child_lst:
        c,depth = child_lst.pop(0)
        if c in tree:
            for nc in tree[c]:
                if alarm[nc]:
                    child_lst.append((nc,depth+1))
                    if authority[nc] >=depth+1:
                        cnt+=1
    return cnt

for q in q_lst:
    if q.cmd ==100:
        idx =0
        for p in q.other[:n]:
            idx +=1
            parent[idx] = p
        idx =0
        for a in q.other[n:]:
            idx +=1
            authority[idx] = a
        # print(parent, authority)
    elif q.cmd ==200:
        c = q.other[0]
        if alarm[c]:
            alarm[c] = False
        else:
            alarm[c] = True
    elif q.cmd ==300:
        c = q.other[0]
        power = q.other[1]
        authority[c]=power
    elif q.cmd ==400:
        c1,c2 = q.other
        parent[c1], parent[c2] = parent[c2], parent[c1]
    elif q.cmd ==500:
        c = q.other[0]
        ans = find_chat(c)
        print(ans)