# 오른쪽으로 밀때는 오른쪽 끝부터 이동
start_point = 0
n,t = map(int,input().split())

lst = []
lst.extend(list(map(int,input().split())))
lst.extend(list(map(int,input().split())))

start_point = (-t)
for idx in range(start_point, start_point+n):
    print(lst[idx%(2*n)], end = ' ')
print()
for idx in range(start_point+n,start_point+2*n):
    print(lst[idx%(2*n)], end = ' ')