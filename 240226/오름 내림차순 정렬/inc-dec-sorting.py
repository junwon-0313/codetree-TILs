n = int(input())
lst = list(map(int, input().split()))

for num in lst:
    print(num, end = ' ')
print()
for num in lst[::-1]:
    print(num, end = ' ')