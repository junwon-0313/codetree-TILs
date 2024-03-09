# 4개의 수열에서 원소를 하나씩 골라 더했을 경우, 합이 0이 되는 경우의 수
# 5000**4
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

first = dict()
for a in range(n):
    for b in range(n):
        num = A[a]+B[b]
        if num in first:
            first[num]+=1
        else:
            first[num]=1

second = dict()
for c in range(n):
    for d in range(n):
        num = C[c]+D[d]
        if num in second:
            second[num]+=1
        else:
            second[num]=1

ans = 0

for k in first:
    if -k in second:
        ans+=first[k]*second[-k]
print(ans)