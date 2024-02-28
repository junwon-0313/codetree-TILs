A = list(input())
B = list(input())
A.sort()
B.sort()
if len(A)!=len(B):
    print('No')
else:
    for idx in range(len(A)):
        if A[idx]!=B[idx]:
            print('No')
            break
    else:
        print('Yes')