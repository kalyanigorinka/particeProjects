import math
from turtle import *
def hearta(r):
    return 15*math.sin(r)**3
def heartb(r):
    return 12*math.cos(r)-5*\
    math.cos(2*r)-2*\
                math.cos(3*r)-\
                math.cos(4*r)
speed(100000000000)
bgcolor("black")
for i in range(10000):
    goto(hearta (i)*20,heartb (i)*20)
    for j in range(5):
        color("#FF0000") 
        goto(0,0)
done()

