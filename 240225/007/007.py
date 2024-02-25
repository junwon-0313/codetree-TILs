class misson:
    def __init__(self, secret_code, meeting_place, time):
        self.s = secret_code
        self.m = meeting_place
        self.t = time
i = list(input().split())
misson1 = misson(i[0],i[1],i[2])
print('secret code :', misson1.s)
print('meeting point :', misson1.m)
print('time :', misson1.t)