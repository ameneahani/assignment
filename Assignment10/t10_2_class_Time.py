class Time:
    def __init__(self,h,m,s):
        self.h = h
        self.m = m
        self.s = s
        self.fix() #har vorodi be tabe ra fix mikonad

    def show(self):
        print(self.h,':',self.m,':',self.s)

    def sum(self, other):
        h = self.h + other.h
        m = self.m + other.m
        s = self.s + other.s
        t = Time(h,m,s)
        t.fix()
        return t
    def fix(self):
        if self.m >= 60:
            self.s -= 60
            self.m +=1

        if self.m >= 60:
            self.m -= 60
            self.h += 1

        if self.s <0:
            self.s += 60
            self.m -= 1

        if self.m < 0:
            self.m += 60
            self.h -= 1




    def save(self):
        ...
    def alarm(self,h,m,s):
        ...
    def difrance(self,h,m,s):
        ...
    def night_or_morning(self):
        ...

t1 = Time(3,75,17)
t1.show()

t2 = Time(4,50,2)
t2.show()

t3 = t1.sum(t2)
t3.show()