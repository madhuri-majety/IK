#! /usr/bin/python3
import math

def mathfunc(func):
    print("The function {} is passed to mathfunc()".format(func.__name__))
    res = 0
    for x in [1,2,2.5]:
        res += func(x)
    return res

print(mathfunc(math.sin))
print(mathfunc(math.cos))
print(mathfunc(math.tan))
