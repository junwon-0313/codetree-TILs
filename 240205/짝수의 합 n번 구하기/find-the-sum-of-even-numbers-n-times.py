n = int(input())
for _ in range(n):
    a,b = map(int, input().split())
    lst = [num if num%2==0 else 0 for num in range(a, b+1)]
    print(sum(lst))