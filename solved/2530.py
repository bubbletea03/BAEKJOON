class TimeManager:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s
    def addSeconds(self, s):
        self.s += s
        while(self.s > 59):
            self.s -= 60
            self.addMinutes(1)
    def addMinutes(self, m):
        self.m += m
        while(self.m > 59):
            self.m -= 60
            self.addHours(1)
    def addHours(self, h):
        self.h += h
        self.h %= 24
    def getTimeArray(self):
        return (self.h, self.m, self.s)


h, m, s = list(map(int, input().split()))
sec = int(input())

time = TimeManager(h, m, s)
time.addSeconds(sec)
for int in time.getTimeArray():
    print(int, end=" ")