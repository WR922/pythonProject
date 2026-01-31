#定义函数
def add(a,b):
    return a+b
print(add(1,2))

print('---------')
#默认参数
def add(x,n=3):
    return x**n
print(add(4))

print('---------')
#*args打包为元组
def add(*args):
    return sum(args)
print(add(1,2,3,4))

print('---------')
#**kwargs打包为字典
def add(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
add(name='王蕊',age=21,sex='女')

print('---------')
#Lambda函数
x=lambda a:a+10
print(x(8))

get_mid=lambda nums:nums[len(nums)//2]
print(get_mid([1,4,5,6,7]))
