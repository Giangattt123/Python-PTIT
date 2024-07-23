s = {1,2,3,4,1,2,3,5}
print(s)
print(len(s))
print(type(s))
## Set Constructor
## Defination a set from a list
a = [1,2,3,4,5,1,2,2]
s1 = set(a)
print(s1)
## Add a element a set
s1.add(6)
print(s1)
## Add more element a set: update
s1.update([1,2,7])
print(s1)
## Delete element in a set
## clear() , remove() , discard() , pop()
s1.discard(1)
print(s1)
# s1.remove(8) ## remove in KeyError if element a not set
## pop(): delete element random in a set
## foreach:O(1) => build hash table
for i in s1:
    print(i , end=" ")
print()
if 2 in s: print("FOUND")
## operations on sets
## union
s2 = s.union(s1)
s3 = s | s1
print(s2)
print(s3)
## intersection: &
## difference: -
## symmetric_difference: ^

## isdisjoint(): Checks whether two sets have common elements or not
## issubset(): tap con
## issuperset(): tap cha

