n = int(input())
stu = []
for idx in range(n):
    h,w = map(int, input().split())
    stu.append([h,w,idx+1])

stu = sorted(stu, key=lambda x:(x[0], -x[1]))
for h, w, idx in stu:
    print(h,w,idx)