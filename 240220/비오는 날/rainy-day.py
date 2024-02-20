n = int(input())
weather = []
for _ in range(n):
    date, day, w = list(input().split())
    year,month, date = date.split('-')
    weather.append([year, month, date, day, w])
weather.sort(key=lambda x:(x[0],x[1],x[2]))

for year, month, date, day, w in weather:
    if w=='Rain':
        t = year+'-'+month+'-'+date
        print(t,day,w)
        break