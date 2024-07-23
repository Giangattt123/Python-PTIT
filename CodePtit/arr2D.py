from random import randrange

## Array to 2D in Python => use nested list
## Init a matrix with 2 row and 3 column
## List normal
print("Mảng 1 chiều bình thường: ")
a = [int(_) for _ in range(2)]
print(a)
## Nested List
a1 = [[1 for _ in range(3)] for _ in range(2)]
print("Mảng 2 chiều: ")
print(a1)
## Input from the keyboard => default a list
for i in range(2):
    a[i] = list(map(int , input().split()))
print(a)
## Through a list
for i in range(2):
    for j in range(3):
        print(a[i][j] , end = " ")
    print()
## Access element in arr 2D
print(a[0][1] , a[1][2])
## Find element max , min in arr 2D
a2 = [[1 , 2 , 5] , [3 , 1 , 0] , [4 , 1 , 5]]
min_val , max_val = 10**18 , -10**18
for row in a2:
    min_val = min(min_val , min(row))
    max_val = max(max_val , max(row))
print(min_val , max_val) # 0 , 5
## Flatten arr2D => arr1D
b = [x for small_list in a2 for x in small_list]
print(min(b) , max(b))
print(b)
## code thuânf
b1 = []
for i in a2:
    for j in i:
        b1.append(j)
print(b1)
## Sum row in a matrix
Sum = [sum(i) for i in a2]
print(Sum)
print(" ".join(map(str , Sum)))
## Create matrix transpose: A -> A(T)
### code chay
aTrans = []
for i in range(len(a[0])):
    row = []
    for j in range(len(a)):
        row.append(a[j][i])
    aTrans.append(row)
print(aTrans)
##3 list comprehension
aTrans2 = [[row[i] for row in a] for i in range(len(a[0]))]
print(aTrans2)

for row in a:
    print(row[0])

### Cộng trừ 2 ma trận
a3 = [[1 , 2 , 3] , [1 , 2 , 3] , [0 , 1 , 2]]
b3 = [[1 , 2 , 3] , [0 , 1 , 2] , [0 , 3 , 4]]
c3 = [[0 for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        c3[i][j] = a3[i][j] + b3[i][j]
print(c3)

## Nhân hai ma trận
n , m , p = map(int , input().split())
a4 , b4 = [0] * n , [0] * m # a4 có n hàng , b4 có m hàng
for i in range(n):
    a4[i] = list(map(int , input().split()))
for i in range(m):
    b4[i] = list(map(int , input().split()))
c4 = [[0 for _ in range(p)] for _ in range(n)]
print(c4)
for i in range(n):
    for j in range(p):
        for k in range(m):
            c4[i][j] += a4[i][k] * b4[k][j]
print(c4)    

"""
Test mẫu a(n*m) ở đây n = 3 m = 3 
5 8 -4
6 9 -5
4 7 -2
Test mẫu b(m*p) ở đây m = 3 p = 1
2
-3
1
Tích 2 ma trận là c(n*p) hay c(3*1)
-18
-20
-15
"""
dong = 3
cot = 4
lst = [[1] * cot]* dong
print(lst)
## Technique for browsing adjacent cells (loang)
