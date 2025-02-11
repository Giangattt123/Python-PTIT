class Phim :
    def __init__(self, ma, theloai, tg, ten, sotap) :
        self.ma = 'P{:03d}'.format(ma)
        self.theloai = theloai
        self.ten = ten
        self.tg = tg
        self.ngay = int(tg[:2:])
        self.thang = int(tg[3:5:])
        self.nam = int(tg[6::])
        self.sotap = sotap
    def __str__(self) :
        return self.ma + ' ' + self.theloai+ ' ' + self.tg + ' ' + self.ten + ' ' + str(self.sotap)

n, m = [int(x) for x in input().split()]
tl = []
p = []
for i in range(n) : tl.append(input())
for i in range(m) :
    id = input()
    ngay = input()
    ten = input()
    sotap = int(input())
    p.append(Phim(i + 1, tl[int(ma[2::]) - 1], ngay, ten, sotap))
p = sorted(p, key = lambda x : (x.nam, x.thang, x.ngay, x.ten, -x.sotap))
for i in range(m) :
    print(p[i])
