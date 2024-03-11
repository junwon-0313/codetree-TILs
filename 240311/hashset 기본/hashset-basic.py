# set()
# add
# remove
# in
n = int(input())
s = set()
for _ in range(n):
    cmd, num = input().split()
    num = int(num)
    if cmd =='find':
        if num in s:
            print('true')
        else:
            print('false')
    elif cmd =='add':
        s.add(num)
    elif cmd=='remove':
        s.remove(num)