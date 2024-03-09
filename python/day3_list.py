'''write a program to build a table (1*1=1) using nested forloop'''
# x=1
# for a in range(1,11):
#     if a>0: print((x),"*",(a),"=",(a*1))


'''write a program using list compherension cubic of list elements'''
#k = [2,2,3,4,5]
#print([i**3 for i in k])#below we return a new list




'''practies list topics'''
# find the list or not
#a = [1,2,3,4,5,6,7,8]
#print(type(a))

# how to find the positive elements?
#a = [67,5,6,8,99,0,7] # forword direction---> 0,1,2,3,4,5,6.... # n-1
#print(a[0]) 

#how to find the negitive elements?
#a = [98,45,23,44,55,66] # backword direction---> -6,-5-,-4,-3,-2,-1...#-n
#print(a[-5])

''' #(s)*3 ...>[start:stop:step]
list = [1,2,3,4,5,6,7,89,56,72,88,89,77,66,79] # 0,1,2,3,4,5,6
print(list[1])
print(list[:3])
print(list[6:])
print(list[4:6]) #..>here print the  index value 4 to 5 elements the last element n-1
print(list[2:6:2]) #..>skip the element'''

'''#list = [1,2,3,4,5,6,7,89,56,72,88,89,77,66,79] #...> -15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1
#print(list[-5])
#print(list[-6:])
#print(list[:-3])
#print(list[-4:-6])
#print(list[-2:-6:-4])'''

#Python List Built-in functions
'''Python provides the following built-in functions, which can
be used with the lists'''

'''#append method
a = [12,33,44,55,66,67]
a.append(0)
print(a)

#extend()
a = [2,3,45,66,99]
a.extend(["ganga",19,300,6778])
print(a)'''

'''#clear()
a = [2,3,45,66,99]
a.clear()
print(a)

#remove()
a = [2,2,3,45,66,99] 
# remove the elements if the spesific value
a.remove(2)
print(a)

#delete()
a = [2,3,45,66,99]
# delete elements only  based on index  num ..>o,1,2,3,..
del a[3]
print(a)'''

'''#pop()
a = [2,3,45,66,99]
a.pop(2) # delete elements only  based on index  num ..>o,1,2,3,.
print(a)

#copy()
a = [2,3,45,66,99]
v=a.copy()
print(v)'''

'''#count()
a = [2,3,2,45,66,99]
print(a.count(2))#find the  repeated element in the given list

#index()
a = [2,3,2,45,66,99]
print(a.index(2)) # find the index value

#insert()
a = [2,3,2,45,66,99]
a.insert(1,"ammu") #a[1]=ammuu secode method 
print(a)'''

# #reverse()
# a = [2,3,2,45,66,99]
# a.reverse()
# print(a)

# #sort()
# a = [2,3,2,45,66,99]
# a.sort()# ascending to discending order
# print(a)
# #sort()2
# a = [2,3,2,45,66,99]
# a.sort(reverse=True)# discending to ascending  order
# print(a)

#sum()
# a = [2,3,2,45,66,99]
# l= sum(a)
# print(l)

# #max() ....> max means big value
# a = [2,3,2,45,66,99]
# l= max(a)
# print(l)

# #min()....>min means small value
# a = [2,3,2,45,66,99]
# l= min(a)
# print(l)

# #list comprehension
# a = [1,2,3,4,5]
# print([i**3 for i in a])











