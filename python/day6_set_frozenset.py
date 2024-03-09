'''set and frozent topics '''

# #find the set or not
# set = {1,2,3,4}
# print(type(set))

# #add()
# set ={1,2,3,4,5}
# set.add(6)
# print(set)

# #clear()
# set ={1,2,3,4,5}
# set.clear()
# print(set)

# #copy()
# set ={1,2,3,4,5}
# set.copy()
# print(set)

# #pop()...>is used to  remove the small element 
# set ={1,2,3,4,5}
# set.pop()
# print(set)

# #remove() is used to the specific value is removed
# set ={1,2,3,4,5}
# set.remove(2)
# print(set)

# #update()
# set ={1,2,3,4,5}
# set.update({45,6})
# print(set)


#set operations
# union().....>is add the value
set1={1,2,34,4,566,67}
set2={7}
print(set1.union(set2))

#intersection().....> is find the only comman values
set1={1,2,3,4,5}
set2={1,2,7}
print(set1.intersection(set2))


#isdisjoin()
set1={1,2,3,4,5}
set2={1,2,}
print(set1.isdisjoint(set2))

#issubset()
set1={1,2}
set2={1,2}
print(set1.issubset(set2))

#issuperset()
set1={1,2}
set2={1,2,5}
print(set1.issuperset(set2))

#difference()
set1={1,2,3,4,5}
set2={1,2,7}
print(set1.difference(set2))

#symmetric_difference()...>same values are not return the output
set1={1,2,3,4,5}
set2={1,2,7}
print(set1.symmetric_difference(set2))


#frozenset()....>find the frozenset or not
s=[1,2,3,4]
b=frozenset(s)
print(type(b))




