A = input()
B = input()
cnt =0
for _ in range(101):
    if A==B:
        print(cnt)
        break
    cnt+=1
    A = A[-1]+A[:-1]
else:
    print(-1)