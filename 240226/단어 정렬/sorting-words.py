n = int(input())
lst = []
for _ in range(n):
    lst.append(input())

lst.sort()
for s in lst:
    print(s)