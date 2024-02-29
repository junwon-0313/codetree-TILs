# 2명의 도둑 -> 처음에는 가장 큰 -> 그다음에는 처음을 제외하고 가장 큰 
# 두 도둑이 각각 최대 무게 ㅊ
# M개의 열중 무게가 C를 넘지 않게 
# 가치 = 무게 **2
# 물건들을 잘 골라 주어진 조건을 만족하면서 얻을 수 있는 가치의 총합 중 최댓값
global n,m,c, ans
ans = 0
n,m,c = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

# 하나의 행에서 연속된 열을 선택하는 방법
def choose(raw: int, col: int, cnt:int, total_gold, option):
    if cnt>m: # m개가 넘으면 종료
        return total_gold
    if (raw,col) in pos:
        return total_gold
    if col<n-1:
        if sum(total_gold)+graph[raw][col]<=c:
            total_gold.append(graph[raw][col])
            if option == 1:
                pos.append((raw,col))


    if col<n-1:
        choose(raw,col+1,cnt+1,total_gold, option)
    return total_gold

# O(n^2*n^2*M) -> 250000
max_pos = []
for raw1 in range(n): # 첫번째 도둑
    for col1 in range(n):
        pos = []
        gold1 =choose(raw1,col1,0,[], 1)
        # 더 비싼 물건이 있을 때, max_pos 업데이트
        for raw2 in range(n): # 두번째 도둑
            for col2 in range(n):
                gold2 = choose(raw2,col2,0,[],2)
                gold_price = 0
                for g in gold1:
                    gold_price+=g**2
                for g in gold2:
                    gold_price+=g**2
                if gold_price>ans:
                    ans=gold_price
print(ans)