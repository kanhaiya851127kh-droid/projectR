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


ages=[10,25,-5,40]
print(list(filter(lambda a:a>0, ages)))


nums=[1,2,3,4,5,6]
ev=list(filter(lambda x:x%2==0, nums))
print(ev)

from functools import reduce
nums=[1,2,3,4]
s = reduce(lambda a,b:a+b, nums)
print(s)


nums=[1,2,3]
res=list(map(lambda x:(x, x*x, x*x*x), nums))
print(res)


ages=[10,25,-5,40]
print(list(filter(lambda a:a>0, ages)))


from functools import reduce
nums=[1,2,3,4]
s = reduce(lambda a,b:a+b, nums)
print(s)


from functools import reduce
nums=[3,9,4,7]
print(reduce(lambda a,b: a if a>b else b, nums))




from functools import reduce

marks = [35,50,80,20,60]

passed = list(filter(lambda x: x>=40, marks))
bonus = list(map(lambda x: x+5, passed))
total = reduce(lambda x,y: x+y, bonus)

print("Passed:", passed)
print("After Bonus:", bonus)
print("Total:", total)



from functools import reduce

nums = [10,45,23,67,12]
maximum = reduce(lambda x,y: x if x>y else y, nums)
print(maximum)


def outer():
    def inner():
        return "Hello"
    return inner

f = outer()
print(f())