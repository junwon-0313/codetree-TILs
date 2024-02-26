n = int(input())
lst = list(map(int, input().split()))
lst.sort()
for num in lst:
    print(num, end = ' ')
print()
for num in lst[::-1]:
    print(num, end = ' ')