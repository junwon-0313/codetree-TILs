a1, a2 = map(int,input().split())
lst = [a1,a2]
for _ in range(8):
    lst.append(lst[-1]+lst[-2]*2)

for i in lst:
    print(i, end = ' ')