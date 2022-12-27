class Complex:
    def __init__(self, real, image):
        self.real = real
        self.image = image

    def show(self):
        print(self.real, '+', self.image, 'i')

    def sum(self,other):
        new_real = self.real + other.real
        new_image = self.image + other.image
        return Complex(new_real, new_image)

    def sub(self,other):
        new_real = self.real - other.real
        new_image = self.image - other.image
        return Complex(new_real, new_image)

    def mul(self,other):
        new_real = self.real*other.real - self.image*other.image
        new_image = self.real*other.image + self.image*other.real
        return Complex(new_real, new_image)

a = Complex(3, 2)
a.show()
b = Complex(1,7)
b.show()
c = a.mul(b)
c.show()
z = b.sub(a)
z.show()
e = a.sum(b)
e.show()