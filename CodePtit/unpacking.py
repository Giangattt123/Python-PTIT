## Unpacking trong python
## là 1 kĩ thuật tách các tuple, list, iterable ra thành các biến rời rạc
## nó khá giống destructuring trong javascript
## List
a = [1,2,3]
x , y , z = a
print(x , y , z)
## Tuple
data = ("Messi" , "CR7" , "Neymar" , "KDB")
name1 , name2 , name3 , name4 = data
print(name1)
## Str
s = "Messi"
a , b , _ , _ , _ = s
print(a , b)
## Range
a , b , c = range(0 , 5 , 2)
print(a , b , c)
## Unpacking với loop for
a1 = [1,2,3,4,5,6,7,8,9,10]
x , y , *z = a1
print(x , y)
print(z)