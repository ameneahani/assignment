
class Time:
    def __int__(self,y,mo,d,h,m,s):
        self.year = y
        self.month = mo
        self.day = d
        self.hour = h
        self.minute = m
        self.second = s





    def save(self):
        ...
    def alarm(self,h,m,s):
        ...
    def difrance(self,h,m,s):
        ...
    def night_or_morning(self):
        ...

zaman = time(1401,10,3,12,20,3)
zaman.alarm(6,30,0)
zaman.night_or_morning()