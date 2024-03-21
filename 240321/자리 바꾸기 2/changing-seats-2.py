n,k = map(int,input().split())

change_lst = []
for _ in range(k):
    ai, bi = map(int,input().split())
    change_lst.append((ai-1,bi-1))

seat = [{i} for i in range(n+1)]
person = [i for i in range(1,n+1)] # 1번 사람이 갈 수 있는 자리

for idx in range(3*k):
    idx = idx%k
    ai, bi = change_lst[idx] # 자리 인덱스, ai번에는 person[ai]사람이 있음
    seat[person[ai]].add(bi+1) # 1번 사람의 자리는 3번 위치가 추가됨 
    seat[person[bi]].add(ai+1) # 3번 사람의 자리는 1번 위치가 추가됨
    person[ai], person[bi]=person[bi], person[ai] # 해당 위치의 값을 바꿈

for s in seat[1:]:
    print(len(s))