n = int(input())
lst = list(map(int,input().split()))

total = []

for idx, num in enumerate(lst):
    total.append(num)
    total.sort()
    if (idx+1)%2==1:
        print(total[len(total)//2], end = ' ')