from collections import deque
import enum

class Element(enum.Enum):
    WATER = 0
    GLACIER = 1
    
# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))

a = [
    list(map(int, input().split()))
    for _ in range(n)
]

# bfs에 필요한 변수들 입니다.
q = deque()
glaciers_to_melt = deque()
visited = [
    [False for _ in range(m)]
    for _ in range(n)
]
cnt = 0

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

# 소요 시간과 가장 마지막으로 녹은 빙하의 수를 저장합니다.
elapsed_time = 0
last_melt_cnt = 0

# 주어진 위치가 격자를 벗어나는지 여부를 반환합니다.
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

# 범위를 벗어나지 않으면서 물이여야 하고 방문한적이 
# 없어야 갈 수 있습니다.
def can_go(x, y):
    return in_range(x, y) and a[x][y] == Element.WATER.value and not visited[x][y]


# 범위를 벗어나지 않으면서 빙하여야 하고 이미 
# 선택된 적이 없어야 중복 없이 녹아야할 빙하 목록에 
# 해당 빙하를 문제 없이 추가할 수 있습니다.
def is_glacier(x, y):
    return in_range(x, y) and a[x][y] == Element.GLACIER.value and not visited[x][y]


# 아직 방문해보지 못한 빙하에 둘러쌓여 있지 않은 물 영역을 더 탐색해주는 BFS입니다.
def bfs():
    while q:
        # queue에서 가장 먼저 들어온 원소를 뺍니다.
        x, y = q.popleft()
        
        # queue에서 뺀 원소의 위치를 기준으로 네 방향을 확인합니다.
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy

            # 더 갈 수 있는 곳이라면 Queue에 추가합니다.
            if can_go(new_x, new_y):
                q.append((new_x, new_y))
                visited[new_x][new_y] = True
            # 만약 아직 방문하지 않은 빙하가 있는 곳이라면
            elif is_glacier(new_x, new_y):
                # 빙하에 둘러쌓여 있지 않은 물에 인접한 빙하이므로 이번에 녹아야 할 빙하이므로 
                # 따로 저장해줍니다.
                # 중복되어 같은 빙하 정보가 기록되는 것을 막기위해
                # 이때에도 visited 값을 true로 설정해줍니다.
                glaciers_to_melt.append((new_x, new_y))
                visited[new_x][new_y] = True


# 녹여야 할 빙하들을 녹여줍니다.
def melt():
    while glaciers_to_melt:
        x, y = glaciers_to_melt.popleft()
        a[x][y] = Element.WATER.value
        
        
# 빙하를 한 번 녹입니다.
def simulate():
    global elapsed_time, last_melt_cnt, q

    # 빙하에 둘러쌓여 있지 않은 물의 영역을 넓혀보며
    # 더 녹일 수 있는 빙하가 있는지 봅니다. 
    bfs()
    
    # 더 녹일 수 있는 빙하가 없다면 시뮬레이션을 종료합니다.
    if not glaciers_to_melt:
        return False
    
    # 더 녹일 빙하가 있다면 답을 갱신해주고
    # 그 다음 시뮬레이션에서는 해당 빙하들의 위치를 시작으로
    # 빙하에 둘러쌓여 있지 않은 물의 영역을 더 탐색할 수 있도록 queue에 
    # 녹아야 할 빙하들의 위치를 넣어줍니다.
    elapsed_time += 1
    last_melt_cnt = len(glaciers_to_melt)

    q = glaciers_to_melt.copy() #!!!!!

    # 녹아야 할 빙하들을 녹여줍니다.
    melt()
    
    return True
    
    
# 처음에는 (0, 0) 에서 시작하여 초기 빙하에 둘러쌓여 있지 않은 물들을 찾을 수 있도록 합니다.
q.append((0, 0))
visited[0][0] = True

while True:
    is_glacier_exist = simulate()
    
    # 빙하에 둘러쌓여 있지 않은 물의 영역을 넓혀보며 더 녹일 수 있는 빙하가 있는지 봅니다.
    if not is_glacier_exist:
        break
        
print(elapsed_time, last_melt_cnt)