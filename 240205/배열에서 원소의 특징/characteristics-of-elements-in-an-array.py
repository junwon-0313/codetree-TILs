lst = list(map(int, input().split()))
for idx,num in enumerate(lst):
    if num%3==0:
        print(lst[idx-1])
        break