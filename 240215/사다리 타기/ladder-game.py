n, m = map(int,input().split()) # n명, m개의 사다리
line = [tuple(map(int,input().split())) for _ in range(m)]

ladder = [[0]*(n+1) for _ in range(16)] # n명 x 최대 길이 15
# 가로 줄 상태 업데이트 -> 왼쪽과 오른쪽 연결을 구분해야함 -> 1로 통일하면 가로줄이 이어짐.
def add_ladder(a,b):
    ladder[b][a],ladder[b][a+1]=1,2
    
def restore_ladder(a,b):
    ladder[b][a],ladder[b][a+1]=0,0

def in_range(x):
    return 1<=x<=n   
# 사다리타기
def ladder_game():
    result = []
    for idx in range(1,n+1):
        seq, h = idx, 0
        # 밑으로 내려가기
        while True:
            if h >15: # 맨 밑에서 종료
                result.append(seq) # 하나씩 순서를 저장
                break
            if ladder[h][seq]==0: # 그대로 내려감
                h+=1
            # 사다리를 타고 내려감, 좌우로 연결된 사다리 찾기
            elif ladder[h][seq]==1: # 1이면 오른쪽으로 이동
                seq = seq+1
                h+=1
            elif ladder[h][seq]==2: # 2이면 왼쪽으로 이동
                seq = seq-1
                h+=1
    return result

ans = 100 # 최대 사다리 수는 15개 이므로 100으로 초기화
# 재귀함수 
def choose(k, cnt): # k번째 사다리, 사용한 사다리 수
    global ans
    # 종료조건
    if k == m:
        final_seq = ladder_game()
        if tuple(final_seq)==tuple(first_seq):
            if ans > cnt:
                ans = cnt
        return
    a, b = line[k]
    # k번째 사다리 선택 안함
    choose(k+1, cnt)

    # k번째 사디리 선택
    add_ladder(a,b)
    choose(k+1, cnt+1)
    restore_ladder(a,b)

for a, b in line:
    add_ladder(a,b)
first_seq = ladder_game()
# print(first_seq)
# for x in range(16):
#     print(ladder[x])

ladder = [[0]*(n+1) for _ in range(16)] # 초기화
choose(0,0)
print(ans)