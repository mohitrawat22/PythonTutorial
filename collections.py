list1 = [2, 3, 'earth', 1.2, True]
print(list1[0:3])
print(list1[-2])
print(list1[1:7:3])

if 1.2 in list1:
    print("true")
else:
    print("false")

# string works like the same
if "rt" in 'earth':
    print("true")
else:
    print("false")

list2 = [i*i for i in range(10)]
list3 = [i*i for i in range(10) if i%2 == 0]

print(list2)
print(list3)


list4 = [11, 45, 1, 2, 4, 6, 1, 1]
print(list4)
list4.append(7)
print(list4)
list4.sort(reverse=True)
print(list4)
print(list4.index(1))
print(list4.count(1))
list4.insert(1, 33)
print(list4)
list5 = list4
list5[0] = 47
print(list4)
print(list5)

list6 = list4.copy()
list6[0] = 49
print(list4)
print(list6)

list7 = [2,4,6]
list8 = [1,3,5]
list9 = list7+list8
print(list9)
list10 = [7,8]
list10.append(list7)
print(list10)
list11 = [8,9]
list11.extend(list7)
print(list11)


# tuples
tup1 = (1)
print(type(tup1), tup1)
tup2 = (1, )
print(type(tup2), tup2)
tup3 = (1,2,3,4,5,6)
# below not possible because tuple is immutable
# tup3[0] = 4
print(tup3[0])
print(tup3[-1])
tup4 = tup3[2:5]
print(tup4)

tup5 = ("spain", "italy", "india", "england", "germany")
list1 = list(tup5)
list1.append("russia")
list1.pop(3)
list1[2] = "finland"
tup6 = tuple(list1)
print(tup6)

# tuples cannot be changed 
# but can be concatenated to a new tuple
tup7 = (1,2,3)
tup8 = (4,5,6)
tup9 = tup7+tup8
print(tup9)

tup1 = (0, 1, 2, 2, 3, 4, 4, 5, 1,2,3,4, 5,6,7)
print(tup1.count(4))
print(tup1.index(4))
# below will cause error because 10 does not exist in the tuple
# print(tup1.index(10))
print(tup1.index(4, 7, 150))
print(len(tup1))

# sets
set1 = {2,3,4,2,5,8,7,3}
print(set1)

# we will make empty dictionary, not empty set
set2 = {}
print(type(set2))

# we will make empty set
set2 = set()
print(type(set2))

# set does not maintain order
# so do not expect that items will come in any order
for i in set1:
    print(i)

set4={3,1,2}
set5={6,8,7}
# it returns new set, does not change existing sets
print(set4.union(set5))
print(set4, set5)

# it adds elements of set5 to set4
set4.update(set5)
print(set4, set5)

set6={1,2,3}
set7={2,3,4}
# elements present in both sets
# returns new set
print(set6.intersection(set7))

# elements present in both sets
# updates existing set
set6.intersection_update(set7)
print(set6, set7)

set8={1,2,3}
set9={2,3,4}
# elements NOT present in both sets
# returns new set
print(set8.symmetric_difference(set9))

# elements NOT present in both sets
# updates existing set
set8.symmetric_difference_update(set9)
print(set8, set9)

set10={1,2,3}
set11={2,3,4}
# elements present in first set NOT in second set
# returns new set
print(set10.difference(set11))

# elements present in first set NOT in second set
# updates existing set
set10.difference_update(set11)
print(set10, set11)

# no elements match
set12={1,2,3}
set13={2,3,4}
print(set12.isdisjoint(set13))

set14={1,2,3}
set15={4,5}
print(set14.isdisjoint(set15))

set16={1,2,3,4,5}
set17={4,5}
print(set16.issuperset(set17))

print(set17.issubset(set16))

# add
set18 = {1,2,3}
set18.add(4)
print(set18)

# remove
set18.remove(4)
print(set18)
# below will throw error, as the value is not present
# set18.remove(6)
# below will NOT throw error even if the value is not present
set18.discard(6)

set19 = {4,5}
set18.update(set19)
print(set18)

# pop
# last item will be popped 
# but we don't know which one will be popped 
# because set is unordered
item = set18.pop()
print(item)

# clears the set and makes it empty
set18.clear()
print(set18)

del set18
# below will throw error because set18 is totally deleted
# print(set18)


# dictionary
dt1 = {"fname": "mohit", "lname": "rawat"}
dt2 = {1: "mohit", 2:"rawat"}
print(dt1["fname"])
print(dt2[2])

# fname1 not present, so it will throw error
# print(dt1["fname1"])
# if we get value using "get" then it will NOT throw error
print(dt2.get(3))

print(dt1.keys())
print(dt1.values())

for key in dt1.keys():
    print(dt1[key])

print(dt1.items())

# item will be key
for item in dt1:
    print(item)

for item in dt1.items():
    print(item)

for key, value in dt1.items():
    print(key, value)

dt3 = {"a": "apple", "b": "ball"}
dt4 = {1: 11, 2: 22}
dt3.update(dt4)
print(dt3, dt4)

dt5 = {"a": "apple", "b": "ball"}
dt6 = {1: 11, 2: 22, "b":"bat"}
dt5.update(dt6)
print(dt5, dt6)

dt6.pop("b")
print(dt6)

dt5.popitem()
print(dt5)

del dt5['a']
print(dt5)

dt5.clear()
print(dt5)

del dt5
# print(dt5)