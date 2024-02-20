n = int(input())
weather=[list(input().split()) for _ in range(n)]

for date, day, w in weather:
    if w=='Rain':
        print(date,day,w)
        break