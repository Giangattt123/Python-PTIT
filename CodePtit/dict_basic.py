## Dictionary: Map in C++, Java, ..
## Tạo dict bằng constructor
a = [['name','giang'], ['job','nodejs'],['age','20']]
b = dict(a)
print(b)
## Tạo dict bằng hàm zip
a1 = ['name' , 'job' , 'age']
b1 = ['giang' , 'nodejs' , '20']
c1 = dict(zip(a1 , b1))
print(c1)
## Tạo dict bằng hàm fromkeys()
a2 = ['a','b','c']
defaultValue= 0
b2 = dict.fromkeys(a2 , defaultValue)
print(b2)
## Truy cập các phần tử của dict
info = {
    'name': 'Giang',
    'job': 'Dev Web',
    'age': 18,
    'dob': '2003'
}
print(info['name'])
print(info.get('name'))
## Duyệt dict => return iterable object
listKey = list(info.keys())
listValue = list(info.values())
listItem = list(info.items())
print(listKey)
print(listValue)
print(listItem)
for key in info.keys():
    print(key , info[key])
for key, value in info.items():
    print(key , value)
## Nếu chỉ duyệt nguyên các key => info
for x in info:
    print(x , end=" ")
print()
## Nếu key đã tồn tại => thay thế value của key
info['age'] = 20
info['exp'] = 2
print(info)
## Xóa 1 cặp key, value => pop(key) , del
## Nếu key không hợp lệ xóa => KeyError
if 'web' in info: info.pop('web')
## popitem() xóa 1 cặp key, value ngẫu nhiên
## Xóa tất cả => clear()
## Trộn 2 dict => update()
## Đếm tần suất xuất hiện sử dụng dict
a3 = [1 , 4 , 6 , 2, 3 , 1 , 2 , 4 , 5 , 2 , 3]
d = dict({})
for x in a3:
    if x in d:
        d[x] += 1
    else:
        d[x] = 1
for x , y in d.items():
    print(x , y)
## b3: list chứa các tuple
b3 = list(d.items())
print(b3)
b3.sort(key = lambda x : x[0])
print(b3)
for item in b3:
    print(item)
## dict comprehension
a4 = [1 ,2 , 3, 4]
d1 = {x : x**2 for x in a4}
print(d1)
## List Comprehension
a5 = [x for x in a4 if x > 2]
a6 = [(lambda x: x > 2)(x) for x in a4]
print(a5)
print(a6)
## Lambda
lam = lambda x : x > 2
res = list(filter(lam , a4))
print(res)
