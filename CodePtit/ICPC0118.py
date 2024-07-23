## CUNG HOÀNG ĐẠO

t = int(input())
for i in range(t):
    day, month = map(int, input().split())
    if month == 1:
        print('Ma Ket' if day < 20 else 'Bao Binh')
    elif month == 2:
        print('Bao Binh' if day < 19 else 'Song Ngu')
    elif month == 3:
        print('Song Ngu' if day < 21 else 'Bach Duong')
    elif month == 4:
        print('Bach Duong' if day < 20 else 'Kim Nguu')
    elif month == 5:
        print('Kim Nguu' if day < 21 else 'Song Tu')
    elif month == 6:
        print('Song Tu' if day < 21 else 'Cu Giai')
    elif month == 7:
        print('Cu Giai' if day < 23 else 'Su Tu')
    elif month == 8:
        print('Su Tu' if day < 23 else 'Xu Nu')
    elif month == 9:
        print('Xu Nu' if day < 23 else 'Thien Binh')
    elif month == 10:
        print('Thien Binh' if day < 23 else 'Thien Yet')
    elif month == 11:
        print('Thien Yet' if day < 23 else 'Nhan Ma')
    else:
        print('Nhan Ma' if day < 22 else 'Ma Ket')

