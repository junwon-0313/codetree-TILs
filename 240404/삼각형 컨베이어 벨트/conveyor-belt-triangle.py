n, t = map(int,input().split())
lst = []
lst.extend(list(map(int,input().split())))
lst.extend(list(map(int,input().split())))
lst.extend(list(map(int,input().split())))
start_point = -t
m = n*3
cnt =0
for idx in range(start_point, start_point+m):
    cnt+=1
    print(lst[idx%m], end = ' ')
    if cnt%n==0:
        print()