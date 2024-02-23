A = input()
cmd = input()
idx =0
for c in cmd:
    if c=='L':
        idx+=1
    else:
        idx-=1
idx=idx%len(A)
print(A[idx:]+A[:idx])