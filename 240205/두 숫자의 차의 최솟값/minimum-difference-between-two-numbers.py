n = int(input())
lst = list(map(int, input().split()))

min_diff = 1e9
for i in range(len(lst)-1):
    tmp_diff = abs(lst[i]-lst[i+1])
    if min_diff>tmp_diff:
        min_diff=tmp_diff
print(min_diff)