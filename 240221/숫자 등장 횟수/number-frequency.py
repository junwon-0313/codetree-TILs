n, m = map(int, input().split())

num_lst = list(map(int, input().split()))
cnt_lst = list(map(int, input().split()))

for num in cnt_lst:
    print(num_lst.count(num), end = ' ')