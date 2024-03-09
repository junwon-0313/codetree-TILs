n, A = input().split()
ans =0
for _ in range(int(n)):
    s = input()
    if A == s:
        ans+=1
print(ans)