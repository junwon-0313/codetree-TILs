n = int(input())
student_lst =[]
for _ in range(n):
    # name, kor, eng, math = 
    student_lst.append(input().split())

student_lst.sort(key=lambda x: (-int(x[1]),-int(x[2]),-int(x[3])))

for name, kor, eng, math in student_lst:
    print(name, kor, eng, math)