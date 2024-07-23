## TÍNH ĐIỂM CHUYÊN CẦN

class ChuyenCan:
    def __init__(self , msv , name , className):
        self.msv = msv
        self.name = name
        self.className = className
        self.point = 0
        self.isCheck = ''
    def getPoint(self , point):
        self.point = max(0 , 10 - (point.count('v') * 2 + point.count('m')* 1))
        if self.point == 0:
            self.isCheck = 'KDDK'
    def __str__(self):
        return f'{self.msv} {self.name} {self.className} {self.point} {self.isCheck}'

def main() -> None:
    n = int(input())
    a = []
    for i in range(n):
        msv = input()
        name = input()
        className = input()
        a.append(ChuyenCan(msv , name , className))
    for i in range(n):
        msv , point = input().split()
        for item in a:
            if item.msv == msv:
                item.getPoint(point)
                break
    for item in a:
        print(item)

if __name__ == '__main__':
    main()

