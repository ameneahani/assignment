

class Fraction:
    #propeties
    def __init__(self,n,d):
        self.n = n #numerator
        while True:
            self.d = d  #denominator
            if self.d != 0:
                break
            else:
                return "cant be zero try again"
         
    #methods
    def sum(self,f2): #fraction
        n = self.n * f2.d + self.d * f2.n
        d = self.d * f2.d
        f = Fraction(n,d)
        return f

    def sub(self):
        ...
    def mul(self,f2):
        f_n = self.n * f2.n
        f_d = self.d *f2.d
        f = Fraction(f_n,f_d)
        return f

    def div(self):
        ...
    def simplify(self):
        ...
    def fraction_to_num(self):
        ...
    def show(self):
        print(self.n,'/',self.d)

a = Fraction(2,3)
a.show()

b = Fraction(7,1)
b.show()

z = a.mul(a,b)
z.show()

e = b.sum(a,b)
e.show()

