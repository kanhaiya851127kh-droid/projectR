add = lambda a, b: a + b
print(add(6, 4))

def apply(f, x):
    return f(x)

print(apply(lambda n: n*n, 5))


nums = [1,2,3,4]
res = list(map(lambda x: x*2, nums))
print(res)