
# # #upper()
# # a = "kalyani"
# # print(a.upper())

# # #lower()
# # a = "KALYANI"
# # print(a.lower())

# # #count
# # a = "this is kalyani"
# # print(a.count("is"))

# #split
# a = "this is kalyani"
# v=a.split()
# print(v.count('is'))# converted to the string to list 

# # #join 
# a = "this is kalyani"
# v=a.split()
# print(v)
# d ="/".join(v)
# print(d)


#join 2
# a = "this is kalyani"
# b = "this is kalyani"
# c=a.split()
# d=b.split()
# print(c,d)
# e = c+d
# r =" ".join(e)
# print(r)

# #find.....>find the index value 
# a = "this is kalyani" #....>including empty space are count 
# print(a.find("is")) 



# #format
# print("my name is {}".format("kalyani"))


# #ex
# a = ["ammu","raju","ranga","ganga","bavani","ganesh","ram","mani","jaggu","neelima","pravallika","deepu"]
# for i in a:
#     print("hey {} thinava".format(i))

# #index...>index value  and including space count 
# a = "this is kalyani"
# print(a.index("kalyani"))

# #strip...> remove the all space 
# a = "     this is kalyani     "
# b = a.strip()
# print(len(b))
# print(b)

# #lstrip....>remove the left side space
# a = "     this is kalyani     "
# b = a.lstrip()
# print(len(b))
# print(b)

# #lstrip....>remove the right side space
# a = "     this is kalyani     "
# b = a.rstrip()
# print(len(b))
# print(b)


# # num=0-9
# # aplha=a-z
# # aplnum=0-9 a-z

# a = "kalyani"
# print(a.isalpha())

# a = "23456788"
# print(a.isnumeric())

# a = "kalyani678"
# print(a.isalnum())

# #title
# a = "kalyani"
# print(a.title())

# #replace
# a = " this is gorinka kalyani" 
# b=a.split()
# c=[]
# for i in b:
#     if i=="is":
#         i="are"
#         c.append(i)
#     else:
#         c.append(i)
#     print(c) 




# a = "hey is u there"
# b=a.split()
# c=[]
# for i in b:
#     if i=="is":
#         i="are"
#         c.append(i)
#     else:
#         c.append(i)
# print(c)




# # using replace()
# python='''Python is an interpreted, object-oriented, high-level programming language
# with dynamic semantics developed by Guido van Rossum. It was originally released in 
# 1991. Designed to be easy as well as fun, that name "Python" is a nod to the British
# comedy group Monty Python.'''

# a=python.replace(" is","are").replace("that","this")
# print(a)


