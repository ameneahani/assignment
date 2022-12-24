

class Fraction:
    #propeties
    def __init__(self,n,d):
        self.numerator = n
        while True:
            self.denominator = d
            if self.denominator != 0:
                break
            else:
                print("cant be zero try again")
         
    #methods
    def add(self):
        ...
    def subtraction(self):
        ...
    def multiple(self):
        ...
    def divide(self):
        ...
    def simplify(self):
        ...