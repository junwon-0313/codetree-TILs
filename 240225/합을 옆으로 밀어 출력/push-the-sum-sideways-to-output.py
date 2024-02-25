n = int(input())
total =0
for _ in range(n):
    total+=int(input())

print(str(total)[1:]+str(total)[0:1])