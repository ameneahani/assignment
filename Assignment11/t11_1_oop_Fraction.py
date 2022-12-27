
import math
class Fraction:
    #propeties
    def __init__(self,n,d):
        self.n = n #numerator
        self.d = d  #denominator
        if self.d == 0:
            raise ZeroDivisionError
        
    #methods
    def sum(self,other): #fraction
        n = self.n * other.d + self.d * other.n
        d = self.d * other.d
        f = Fraction(n,d)
        return f

    def sub(self,other):
        i = -other.n
        f = Fraction(i,other.d)
        return self.sum(f)
         
    def mul(self,other):
        n = self.n * other.n
        d = self.d *other.d
        f = Fraction(n,d)
        return f

    def div(self,other):
        i = other.d
        j = other.n
        f = Fraction(i,j)
        return self.mul(f)

    def fraction_to_num(self):
        num = self.n / self.d
        print('num = ',num)
        return num

    def simplify(self):
        gcd = math.gcd(self.n, self.d)
        n = self.n// gcd
        d = self.d// gcd
        return Fraction(n,d)

    def show(self):
        print(self.n,'/',self.d)

a = Fraction(2,4)
a.show()

b = Fraction(7,1)
b.show()

e2 = a.sum(b)
e2.show()

e3 = a.sub(b)
e3.show()

e1 = a.mul(b)
e1.show()

e4 = a.div(b)
e4.show()

e5 = a.fraction_to_num()

e6 = a.simplify()
e6.show()
