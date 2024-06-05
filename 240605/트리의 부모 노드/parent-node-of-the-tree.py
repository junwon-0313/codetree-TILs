n = int(input())
tree = {}
tree[1]=[]
for _ in range(n-1):
    a, b = map(int,input().split())
    if a in tree:
        tree[b]=[]
        tree[a].append(b)

    elif b in tree:
        tree[a]=[]
        tree[b].append(a)

for num in range(2,n+1):
    for k,v in tree.items():
        for v_tems in v:
            if v_tems==num:
                print(k)
                break