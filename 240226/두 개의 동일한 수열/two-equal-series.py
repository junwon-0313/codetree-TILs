n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
B.sort()
for idx in range(n):
    if A[idx]!=B[idx]:
        print('No')
        break
else:
    print('Yes')