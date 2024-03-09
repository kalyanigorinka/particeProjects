'''      object oriented programming     '''


# class(template)
'''
1.we will define class by using 'class' keyword
2.blue print to create a objects
3.collection of objects is called class
'''
#ex fruits


# object
# physical entity(real)
'''
1.an instance of a class
2.memory is created when it declared
'''
#ex apple,orange,mango


# self keyword
'''
we can access the attributes and methods of the class(current class only)
'''

# class Ammu(): #class defination 
#     def class_fun(priya):
#         print("this is class fun")
#         print("hi")
# #object name = class name()
# obj=Ammu()
# #obj.method
# obj.class_fun()

# ex 2

# class Ganga():
#     a=100
#     def show(self):
#        print("hello")
# kalyani=Ganga()
# print(kalyani.a)
# kalyani.show()



'''
# # # __init__

# # Constructors are generally used for instantiating an object. 
# # The task of constructors is to initialize(assign values)
# # to the data members of the class when an object of the class 
# # is created.
# # In Python the __init__() method is called the constructor
# # and is always called when an object is created

# # does'nt support multiple constructor
# # 
'''
# class Car():
#     def __init__(self,Car_Name,CC,Price,Color,Mileage):
#         self.a=Car_Name
#         self.b=CC
#         self.c=Price
#         self.d=Color
#         self.e=Mileage

#     def car_details(self):
#         print("Car_Name:",self.a)
#         print("CC:",self.b)
#         print("Price:",self.a)
#         print("Color:",self.a)
#         print("Mileage:",self.a)
        
# while True:# while loop are used
#   cn=input("enter the car_name:")
#   cc=input("enter the cc:")
#   p=input("enter the price:")
#   c=input("enter the color:")
#   m=input("enter the mileage:")


#   carobj=Car(cn,cc,p,c,m)
#   carobj.car_details()

'''
# # inheritance
# # single (parent child)
# # multiple(two are more base classes)
# # # multilevel(tree)
# # # # hierarchical(one base with sibiling childs)

'''

# class Priya:
#     def Outupt(self):
#         print("hello")
# class Ammu(Priya):
#     def Output1(self):
#         print("hello")
# obj=Ammu()
# obj.Outupt()
# obj.Output1()


# class Priya:
#     def Outupt(self):
#         print("this is priya")
# class Ammu:
#     def Output1(self):
#         print("this is ammu")
# class Ranju(Priya,Ammu):
#     def OutputRanju(self):
#         print("this is ranju")

# i=Ranju()
# i.Outupt()
# i.Output1()
# i.OutputRanju()



'''# Polymorphism
# poly-many
# morph = forms
# 1.method overloading 
# 2.method overridding'''




# class overlod:
#     def stg(self,a=None,b=None,c=None):
#         print(a,b,c)
# obj=overlod()
# obj.stg(10,23,44)
# obj.stg(10,12)
# obj.stg(1)
# obj.stg()




# class Methodoverri:
#     def display(self):
#         print("this is parent class")

# class Child(Methodoverri):
#     def display(self):
#         print("this is child class")
#         super().display() 

# class Child2(Child):
#     def display(self):
#         print("this is child 2 class")
#         super().display() 
               
# obj=Child2()
# obj.display()





'''
#encapsulation

# binding of class (methods and variables(attributes))
# # public 
# # and 
# # private __
# # protected _
'''



# class priya:
#     def __init__(self,a):
#         self._y=a
#         print(self._y)
# class priyanka(priya):
#     def display1(self):
#         print(self._y)
# class sis(priyanka):
#     def display2(self):
#         print("sis",self._y)
# obj=sis(12)
# obj.display1()
# obj.display2()


'''
# #abstraction
#abstract method there is no body
#abstract base class can not  create object
#a class contain one or more abstract methods then it said to be a abc
'''

# Python program demonstrate  
# abstract base class work  


from abc import ABC, abstractmethod   
class bike(ABC): 
    @abstractmethod  
    def mileage(self):   
        pass  
class Pura_Adrenalina(bike):   
    def mileage(self):   
        print("The mileage is 20kmph")   
class Zeus(bike):   
    def mileage(self):   
        print("The mileage is 25kmph ")   
class hero(bike):   
     def mileage(self):   
          print("The mileage is 24kmph ")   
class T_Rider(bike):   
    def mileage(self):   
            print("The mileage is 27kmph ")  

# # Driver code

p= Pura_Adrenalina()   
p.mileage()   
z=Zeus()
z.mileage()
h=hero()
h.mileage()
t=T_Rider()
t.mileage()



