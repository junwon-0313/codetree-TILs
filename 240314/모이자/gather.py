n = int(input())
lst = list(map(int,input().split()))

ans =1e9
for pos in range(n): # 집을 선택
    total_distance = 0
    for idx, people in enumerate(lst):
        total_distance+=abs(idx-pos)*people
    if total_distance<ans:
        ans=total_distance
print(ans)