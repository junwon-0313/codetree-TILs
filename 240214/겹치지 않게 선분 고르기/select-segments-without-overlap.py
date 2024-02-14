n = int(input())
line = [tuple(map(int, input().split())) for _ in range(n)] # 선분의 정보
points = [False for _ in range(1001)] # 해당 점을 이미 방문했는지, 전역 변수

def overlap(x1,x2):
    for point in range(x1,x2+1):
        if points[point]:
            return True
    else:
        return False
def add_line(x1,x2):
    for point in range(x1,x2+1):
        points[point]= True

ans = 0
# k번째 선분을 선택하여 추가하는 재귀 함수
def choose(k: int, count: int):
    global ans, points
    # 종료 조건
    if k ==n:
        if count> ans:
            ans = count
        return
    x1, x2 = line[k]
   
    if overlap(x1,x2): # 겹칠 경우
        choose(k+1, count)
    else: # 겹치지 않을 경우
        # 선분 추가
        tmp = points[:]
        add_line(x1,x2)
        choose(k+1, count+1)

        points = tmp[:]
        # 그대로 진행
        choose(k+1, count)



choose(0,0)
print(ans)