'''list =[]
for i in range (5):
    n = int(input("enter number "))
    list.append(n)
print(list)

list = [1,2,3]
list.append(4)
print(list)

lst = [10,20,30]
lst.remove(20)
print(lst)


lst =[3,1,5,2]
lst.sort()
print("ascending :", lst)
lst.sort(reverse = True)
print("descending :",lst )

lst = [1,2,3]
New = [ ]
for i in lst :
    New =[i]+New
print(New)

name = ["ram","amit","karan"]
name.sort()
print(name)


a = [1,2]
b = [3,4]
c = a+b
print(c)


lst = [ 1,2,3,4]
even = [ ]
odd = [ ]
for i  in lst :
    if i % 2 == 0 :
        even.append(i)
    else:
        odd.append(i)
    print("even :",even)
   
    print("odd :",odd)


mat = [1,2] , [3,4]
for row in mat :
    print(row) 

lst = [10,20,30]
m = max (lst)
lst.remove(m)
print(max(lst))

a = [1,2,3,]
b = [2,3,4,]
for i in a :
    if i in b :
        print(i)

t = (10,20,30,40,50)
print( "first element :" , t[0])
print( "last element :" , t[-1])


lst = [ 1,2,3]
t = tuple(lst)

print("tuple :",t)



t = [10,20,30]
print(t.index(30))

t = [10,20,30]
n = 20
if n in t :
    print("presnt")
else:
    print ("not present")

t = [2,3,4]
p = 1
for i in t :
    p *= i
print(p)'''


t =  (1,(2,3),4)
for i in t :
    if isinstance(i, tuple ):
        print("nested tuple present")
        break
    else:
        print("not nested")