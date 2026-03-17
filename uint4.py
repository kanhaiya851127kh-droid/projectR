sq = [x*x for x in range(1,11)]
print(sq)


s = "education"
v = {ch for ch in s if ch in "aeiou"}
print(v)


d = {x: x**3 for x in range(1,6)}
print(d)



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



def country(name="India"):
    print(name)

country()


def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)

print(fib(6))


def report(*marks, **details):
    print("Name:", details["name"])
    print("Total:", sum(marks))

report(80,90,85,name="Kanhaiya")



def info(name, age=18, city="Jamshedpur"):
    print(name, age, city)

info("Kanhaiya", city="Ranchi")



def add(a, b):
    return a + b

print(add(3, 4))


def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True


print(is_prime(7))