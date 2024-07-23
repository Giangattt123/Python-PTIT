## LỚP POINT

from math import *
class Point:
    def __init__(self , X , Y):
        self.X = X
        self.Y =Y
    def distance(self , other):
        return '{:.4f}'.format(sqrt((self.X - other.X) ** 2 + (self.Y - other.Y) ** 2))

def Decimal(num):
    return float(num)

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1