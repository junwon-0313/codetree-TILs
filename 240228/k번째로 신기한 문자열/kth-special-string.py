n, k, t = input().split()
lst = []
for _ in range(int(n)):
    s = input()
    if len(s)>=len(t) and s[:len(t)]==t:
        lst.append(s)

lst.sort()
print(lst[int(k)-1])