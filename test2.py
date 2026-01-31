a,b=0,1
while a<1000:
    print(a,end=',')
    a,b=b,a+b

print('\n----------------------')

r=25
area=3.1415*r*r
print(f"area={area:.2f}")

##print('\n----------------------')
##
##from turtle import *
##color('red','red')
##begin_fill()
##for i in range(5):
##    fd(200)
##    rt(144)
##end_fill()
##done()

print('\n----------------------')

import time
limit=10*1000*1000
start=time.perf_counter()
while True:
    limit=limit-1
    if limit<=0:
        break
delta=time.perf_counter() - start
print(f"程序运行时间是：{delta:.3f}秒")

# print('\n----------------------')
#
# import turtle
# colors=['red','orange','yellow','green','blue','indigo','purple']
# for i in range(7):
#     c=colors[i]
#     turtle.color(c,c)
#     turtle.begin_fill()
#     turtle.rt(360/7)
#     turtle.circle(50)
#     turtle.end_fill()
# turtle.done()
