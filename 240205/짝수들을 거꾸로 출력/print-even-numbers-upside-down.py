n = int(input())
lst = list(map(int, input().split()))
for num in lst[::-1]:
    if num %2==0:
        print(num, end= ' ')