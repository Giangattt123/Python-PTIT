## TÍNH ĐIỂM TRUNG BÌNH

n = int(input())
a = [float(i) for i in input().split()]
Min , Max = max(a) , min(a)

point = []
for i in a:
    if i != Min and i != Max:
        point.append(i)
print("{:.2f}".format(sum(point) / len(point)))

