list =[]
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


