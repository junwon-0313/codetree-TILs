# 새로운 temp 배열을 만든다.
# 아래에서 올라오면서 비어있지 않을 때만 넣어준다.
# temp 값을 기존 배열에 다시 옮겨준다.

n =int(input())
lst = []
for _ in range(n):
    num = int(input())
    lst.append(num)


for _ in range(2):
    start, end = map(int,input().split())
    for idx in range(start-1, end):
        lst[idx]=-1
    new_lst = []
    for num in lst:
        if num!=-1:
            new_lst.append(num)
    lst = new_lst[:]
print(len(lst))
for num in lst:
    print(num)