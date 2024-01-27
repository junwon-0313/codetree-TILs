total = []
while True:
    s = int(input())
    if s//10!=2:
        print(f'{sum(total)/len(total):.2f}')
        break
    total.append(s)