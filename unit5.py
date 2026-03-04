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




nums = [1,2,3,4,5,6]
even = list(filter(lambda x: x%2==0, nums))
print(even)

def apply_func(func, lst):
    return [func(x) for x in lst]

print(apply_func(lambda x: x+5, [1,2,3]))




nums = [1,2,3]
result = list(map(lambda x: (x, x**2, x**3), nums))
print(result)


add = lambda a, b: a + b
print(add(5, 3))



sum_two = lambda x, y: x + y
print(sum_two(10, 20))



def operate(func, a, b):
    return func(a, b)

result = operate(lambda x, y: x * y, 4, 5)
print(result)



nums = [1,2,3,4]
double = list(map(lambda x: x*2, nums))
print(double)



nums = [1,2,3,4,5,6]
even = list(filter(lambda x: x%2==0, nums))
print(even)




nums = [1,2,3,4]
total = reduce(lambda x,y: x+y, nums)
print(total)




nums = [1,2,3,4]
squares = list(map(lambda x: x**2, nums))
print(squares)



nums = [1,2,3,4,5,6]
odd = list(filter(lambda x: x%2!=0, nums))
print(odd)



nums = [10,20,30]
result = reduce(lambda x,y: x+y, nums)
print(result)



square = lambda x: x*x
print(square(6))



def apply_func(func, lst):
    return [func(x) for x in lst]

print(apply_func(lambda x: x+5, [1,2,3]))



celsius = [0,10,20]
fahrenheit = list(map(lambda c: (c*9/5)+32, celsius))
print(fahrenheit)




words = ["apple","banana","mango","watermelon"]
long_words = list(filter(lambda x: len(x)>5, words))
print(long_words)




nums = [1,2,3,4]
product = reduce(lambda x,y: x*y, nums)
print(product)



words = ["kanhaiya","kumar"]
upper = list(map(lambda x: x.upper(), words))
print(upper)



nums = range(2,20)

prime = list(filter(lambda x: all(x%i!=0 for i in range(2,x)), nums))
print(prime)



from functools import reduce

words = ["Hello","World"]
result = reduce(lambda x,y: x+" "+y, words)
print(result)




max3 = lambda a,b,c: a if (a>b and a>c) else (b if b>c else c)
print(max3(10,25,15))



def outer():
    def inner():
        return "Hello"
    return inner

f = outer()
print(f())



nums = [1,2,3]
result = list(map(lambda x: (x, x**2, x**3), nums))
print(result)



data = [1,2,2,3,-1,4,-2,5]
clean = list(filter(lambda x: x>0, set(data)))
print(clean)



from functools import reduce

nums = [10,45,23,67,12]
maximum = reduce(lambda x,y: x if x>y else y, nums)
print(maximum)



lists = [[1,2],[3,4]]
result = list(map(lambda lst: list(map(lambda x: x*2, lst)), lists))
print(result)



marks = [35,50,80,20,60]
passed = list(filter(lambda x: x>=40, marks))
print(passed)



from functools import reduce

marks = [35,50,80,20,60]

passed = list(filter(lambda x: x>=40, marks))
bonus = list(map(lambda x: x+5, passed))
total = reduce(lambda x,y: x+y, bonus)

print("Passed:", passed)
print("After Bonus:", bonus)
print("Total:", total)