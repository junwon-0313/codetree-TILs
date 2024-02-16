# 그래프란 정점과 간선으로 이루어져 있는 자료구조
# 인접 행렬
# 인접 리스트 -> V 개의 동적 배열 -> V+E
# 깊이 우선 탐색 -> 쭉 들어갔다가 나오는 방법
# DFS는 재귀함수 -> 메모리의 Stack 구조 활용
# 출력, 방문, 재귀
# 그래프 탐색 알고리즘의 대원칙 
# 1. 시작점으로부터 연결된 모든 정점을 방문해야함.
# 2. 이미 방문했을 경우, 다시 방문 x
n, m = map(int, input().split())
adjacent_list = [[] for _ in range(1001)] # 인접 리스트 사용
for _ in range(m):
    x,y = map(int, input().split())
    adjacent_list[x].append(y)
    adjacent_list[y].append(x)

def dfs(v):
    global total
    for adj_v in adjacent_list[v]:
        if not visited[adj_v]:
            total+=1
            visited[adj_v]=True
            dfs(adj_v)
global ans
ans =0 
for idx in range(1,1001):
    total =0
    visited = [False for _  in range(1001)]
    visited[idx]=True
    dfs(idx)
    if total>ans:
        ans = total
print(ans)