'''r=read funtion'''

# f=open("file.txt",mode="r")
# c = f.read()
# print(c)
# f.close()

'''w=write funtion'''


# f=open("file.txt",mode="w")
# f.write("this is write funtion")
# f.close()


'''
read=total data
read lines=data in list form
read line=only one line
'''



# f=open("adc.json",mode="r")
# content=f.read(10)
# print(content)
# f.close()



'''a=append funtion'''


# f=open("demo.txt",mode="a")
# f.write(" this is append mode")
# f.close()


'''
read=total data
read lines=data in list form
read line=only one line
'''


# file=open("demo.txt",mode="r")
# c=file.readlines()
# print(c)
# file.close()




'''Reading file in ‘r+’ mode:'''

# with open('demo.txt','r+') as fd:
#     print(fd.tell())
#     print(fd.read())
#     print(fd.tell())


'''Reading file in ‘w+’ mode'''

# with open('demo.txt','w+') as fd:
#     print(fd.tell())
#     c=fd.write("this is w+")
#     print(fd.read())
#     print(fd.tell())
  



'''Write file in ‘r+’ mode'''

# with open('demo.txt','r+') as fd:
#     fd.write("New text.")


'''
r+= read and write(starts 0 )   abcan
w+=write and read(data replace) abc


'''


# Write file in ‘w+’ mode
# with open('demo.txt','w+') as fd:
#     fd.write("New text.")



# with open('sample2.txt','r+') as fd:
#     pass

#Opening file in ‘w+’ mode when it does not exist
# with open('sample1.txt','w+') as fd:
#     pass
    



'''
tell() method can be used to get the position of File Handle. 
tell() method returns current position of file object.
This method takes no parameters and returns an integer value. 
'''



# Python program to demonstrate
# tell() method


# Open the file in read mode
# fp = open('demo.txt', "r")

# # # Print the position of handle
# print(fp.tell())

# # #Closing file
# fp.close()



# # Python program to demonstrate
# # tell() method

# Opening file
# fp = open('demo.txt', "r")
# fp.read(8)

# # # Print the position of handle
# print(fp.tell())

# # # Closing file
# fp.close()



 
'''
seek() function is used to change the position of the File Handle to a given specific position. 
File handle is like a cursor, which defines from where the data has to be read or written in the file. 
'''

'''
f.seek(0)	
Move file pointer to the beginning of a File
'''





# # # Opening file
# fp = open('demo.txt', "r")
# print(fp.tell()) # 0
# fp.read(2) # 2

# # # # # Print the position of handle
# print(fp.tell())   # 2
# fp.seek(0) # 0
# print(fp.tell())  #0

# # # # # Closing file
# fp.close()







# file=open('demo.txt',mode='r+') # open
# content=file.read() # operation
# v=str(content)
# print(v)
# f=v.split()
# print(f)
# f.insert(2,'  chetan')
# print(file.tell())
# file.close()
# file=open('demo.txt',mode='w')
# print(f)
# for i in f:
#     file.writelines([i])


# f=open(r"C:\Users\kiran\Desktop\PythonLife_Batches\Feb_batch_2023\demo\another.txt",mode="r")
# c=f.read()
# print(c)
# f.close()


# import os     
# print(os.getcwd())