A = input()
cmd = input()
idx =0
for c in cmd:
    if c=='L':
        idx+=1
    else:
        idx-=1

if idx>=0:
    print(A[idx:]+A[:idx])
else:
    print(A[idx:]+A[:idx+len(A)])