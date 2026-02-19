'''add = lambda a, b: a + b
print(add(6, 4))

def apply(f, x):
    return f(x)

print(apply(lambda n: n*n, 5))


nums = [1,2,3,4]
res = list(map(lambda x: x*2, nums))
print(res)'''


from functools import reduce
marks=[30,55,80,20,90]
passed=list(filter(lambda m:m>=40, marks))
scaled=list(map(lambda m:m+5, passed))
total=reduce(lambda a,b:a+b, scaled)
print(total)


lst=[[1,2],[3,4]]
res=list(map(lambda sub:list(map(lambda x:x*2, sub)), lst))
print(res)


def outer():
    x=5
    def inner():
        print(x)
    inner()
outer()


import math
print(math.pow(2,3))
print(math.ceil(2.3))