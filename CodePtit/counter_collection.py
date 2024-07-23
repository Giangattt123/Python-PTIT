from collections import Counter, OrderedDict
a = [1,2,5,2,3,3,4,1]
b = Counter(a)
print(b)
dic = list(dict(Counter(a)).items())
print(dic)
