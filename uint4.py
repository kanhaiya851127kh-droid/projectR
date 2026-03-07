'''sq = [x*x for x in range(1,11)]
print(sq)


s = "education"
v = {ch for ch in s if ch in "aeiou"}
print(v)


d = {x: x**3 for x in range(1,6)}
print(d)
'''


def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)

print(fib(6))



def student(name, age):
    print(name, age)

student(age=20, name="Rahul")


def student(name, age):
    print(name, age)

student(age=20, name="Rahul")