n = int(input())

d = dict()
for _ in range(n):
    cmd = input().split()
    if  cmd[0]== 'add':
        d[cmd[1]]=cmd[2]
    elif cmd[0] == 'find':
        if cmd[1] in d:
            print(d[cmd[1]])
        else:
            print(None)
    elif cmd[0] =='remove':
        d.pop(cmd[1])