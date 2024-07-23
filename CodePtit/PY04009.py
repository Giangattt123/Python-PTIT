## LỚP SỐ PHỨC

class Complex:
    def __init__(self, real, virtual):
        self.real = real
        self.virtual = virtual

    def add(self, o):
        a = self.real + o.real
        b = self.virtual + o.virtual
        return Complex(a, b)

    def multi(self, o):
        a = self.real * o.real - self.virtual * o.virtual
        b = self.real * o.virtual + self.virtual * o.real
        return Complex(a, b)

    def __str__(self):
        if self.virtual >= 0:
            return f"{self.real} + {self.virtual}i"
        else:
            return f"{self.real} - {-self.virtual}i"


t = int(input())
while t > 0:
    a = [int(i) for i in input().split()]
    b = Complex(a[0], a[1])
    c = Complex(a[2], a[3])
    d = b.add(c)
    print(d.multi(b), end=", ")
    print(d.multi(d))
    t -= 1