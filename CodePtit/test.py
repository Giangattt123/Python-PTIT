## Tạo ra 1 list các bit

# a = "GIANG"
# print(a[:-1])
# print(a[::-1])
#
# s = "  mcs   "
# print(s.strip())
# print(len(s.strip()))

# a = float(40)
# b = float(4.25)
#
# a /= 2 if a > 10 else 1
# b /= 2 if b > 10 else 1
# print(a , b)
#
# c  = [1 , 2 , 3 , 3 , 2 , 1 , 3, 4]
# c.pop()
# print(c.count(3))
# print(c)
# a  = [1 , 2, 3 , 2 , 3 , 1]
# print(a.index(7))

# import time
# def countdown():
#     for i in range(60 , -1 , -1):
#         print(i)
#         time.sleep(1)
#     print("Happy New Year 2024")
# countdown()

# a = "hELLo"
# print(a.title())
# print(a.capitalize())

# a  = [1,2,3,4,5]
# x , y , z , *t = a
# print(x , y , z , t)

# a = 12.234345
# s1 = f'{a:.2f}'
# print(a)
# print(type(a))

# def my_function(**kwargs):
#     for key , value in kwargs.items():
#         print(key + ":" + str(value))
# my_function(name="Giang",age=20,city="haNoi")

# all_methods = dir(list)
# for value in all_methods:
#     if not value.startswith('__'):
#         print(value)

# a = 25
# def my_func():
#     prefix = "value of 'a' is"
#     print(f'{prefix} {a}')
# my_func()

# a = 25
# def my_func():
#     global a
#     prefix = "value of 'a' is"
#     print(f'{prefix} {a}')
#     a = 35 # chỉ được tạo khi hàm được thực thi
#     # một biến mang tính cục bộ khi ta gán chúng trong hàm
# my_func()
# print(a)

# s  : str = "   Hi  hello giang   Dev   "
# print(s.strip())

## work with time
# from datetime import datetime , time
# now: datetime = datetime.now()
# print(now)
# print(f'{now:%d.%m.%y}')
# data_spec: str = '%d.%m.%y'
# print(f'{now:{data_spec}}')
#
# my_list = [1,2,3,4,5,6,7]
# my_list_1  = [i for i in my_list if i % 2 == 0]
# print(my_list_1)
#
# my_list_2 = [i for i in my_list if (lambda x: x % 2 == 0)(i)]
# print(my_list_2)

# filter vs map , filter vs lambda

## Ways to enter 2-dimensional arrays

# n = int(input())
# a = [[]] * n
# for i in range(n):
#     a[i] = [int(j) for j in input().split()]
# print(a)
#
# b = [[0 for i in range(n)] for _ in range(n)]
# for i in range(n):
#     b[i] = list(map(int , input().split()))
# print(b)
#
# c = []
# for i in range(n):
#     c.append(list(map(int , input().split())))
# print(c)

# a = [0]
# a1 = [1 , 2 , 3, 4]
# print(a + a1)
n = 4
print(bin(n), bin(n)[2:])


