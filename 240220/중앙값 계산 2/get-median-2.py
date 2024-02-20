n = int(input())
lst = list(map(int,input().split()))

total = []

for num in lst:
    total.append(num)
    total.sort()
    if num%2==1:
        print(total[len(total)//2], end = ' ')