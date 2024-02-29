# 2명의 도둑이 동시에 선택
# O(N^2*N^2)
global m, c
n,m,c = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

def choose(lst, gold_lst, k): # k번째 자리의 수를 선택
    global max_gold
    if k==len(lst):
        tmp_gold =0
        for gold in gold_lst:
            tmp_gold+=gold**2
        if tmp_gold> max_gold:
            max_gold = tmp_gold
        return max_gold
    # 그냥 진행
    choose(lst, gold_lst,k+1)
    if sum(gold_lst)+lst[k]<=c:
        # 범위를 넘어서지 않을 때 추가
        gold_lst.append(lst[k])
        choose(lst, gold_lst,k+1)
        gold_lst.pop()
    return max_gold

total_gold=0
for x1 in range(n):
    for y1 in range(n):
        for idx in range(m):
            pos =[] # 두 도둑이 겹치지 않게 관리
            pos.append((x1,y1+idx))
        max_gold = 0 # M개 중에서 선택해서 가장 큰 경우
        gold1 = choose(graph[x1][y1:y1+m], [], 0)
        for x2 in range(n):
            for y2 in range(n):
                if (x2,y2) in pos:
                    continue
                max_gold = 0
                gold2 = choose(graph[x2][y2:y2+m], [], 0)
                if gold1+gold2>total_gold:
                    total_gold=gold1+gold2

print(total_gold)