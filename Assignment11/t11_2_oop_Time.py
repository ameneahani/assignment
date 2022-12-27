class Time:
    def __init__(self,h,m,s):
        self.h = h
        self.m = m
        self.s = s
        self.fix() 

    def show(self):
        print(self.h,':',self.m,':',self.s)

    def fix(self):
        while self.s>=60 or self.m>=60 or self.s<0 or self.m<0:
            if self.s >= 60:
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

    def sum(self, other):
        h = self.h + other.h
        m = self.m + other.m
        s = self.s + other.s
        t = Time(h,m,s)
        return t

    def sub(self,other):
        h = self.h - other.h
        m = self.m - other.m
        s = self.s - other.s
        return Time(h,m,s)

    def conv_to_second(self):
        second = self.h*3600 + self.m*60 + self.s
        print('second = ',second)
        return second
        
    def GMT_to_Iran(self):
        other = Time(3,30,0)
        return self.sum(other)

t1 = Time(3,75,17)
t1.show()

t2 = Time(4,50,2)
t2.show()

t3 = t1.sum(t2)
t3.show()

t4 =Time(0,0,3600)
t4.show()

t5 = Time(12,36,15)
t6 =t5.GMT_to_Iran()
t6.show()