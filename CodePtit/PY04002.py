## LỚP RECTANGLE

from math import *

class Rectangle:
    def __init__(self, chieuDai, chieuRong, mauSac):
        self.chieuDai = chieuDai
        self.chieuRong = chieuRong
        self.mauSac = mauSac

    def perimeter(self):
        return (self.chieuDai + self.chieuRong) * 2

    def area(self):
        return self.chieuDai * self.chieuRong

    def color(self):
        return self.mauSac.lower().title()

arr = input().split()
if int(arr[0]) > 0 and int(arr[1]) > 0:
    r = Rectangle(int(arr[0]), int(arr[1]), str(arr[2]))
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
else: print('INVALID')
