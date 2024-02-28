# 객체 정렬, 익명함수 lambda
n = int(input())
lst = []
for _ in range(n):
    tmp = input().split()
    lst.append(tmp)
lst.sort(key=lambda x:x[1])
for name, height, weight in lst:
    print(name, height, weight)