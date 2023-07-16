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

