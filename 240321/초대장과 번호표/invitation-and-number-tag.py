# k-1명이 초대장을 받았으면 나머지 한사람도 무조건 받는다.
n,g = map(int,input().split())
group = []
visited = [False for _ in range(g)]
for _ in range(g):
    g_lst = list(map(int,input().split()))
    group.append(set(g_lst[1:]))
invest = {1}

while True:
    cnt =0
    for idx, s in enumerate(group):
        if visited[idx]:
            continue
        if len(s-invest)==1:
            invest = invest | (s-invest)
            visited[idx]=True
            cnt+=1
    if cnt==0:
        break

# print(invest)
print(len(invest))