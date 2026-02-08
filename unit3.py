'''s ={1,2,3,4,5}
print(s)

s ={1,2,3,}
s.add(4)
s.remove(2)
print(s)

a ={1,2,}
b ={3,4,}
print(a|b)


s ={10,5,30}
print(max(s))
print(min(s))

lst =[1,2,2,3]
print(len(set(lst)))

s = "hello hi hello"
words = s.split()       
unique_words = set(words)
print(unique_words)

a ={1,2}
b ={3,4}
print(a.isdisjoint(b))

a ={1,2,3}
b ={2,3,4}
for i in a :
    if i in b :
        print(i)


d = {"ram" : 80 ,"amit" : 90 ,"kanhaiya" : 70}
print(d)

d = {"ram" : 80 ,"amit" : 90 ,"kanhaiya" : 70}
d ["ram"] = 85

print(d)

d = {"ram" : 80 ,"amit" : 90 ,"kanhaiya" : 70}
del d ["amit"]
print(d)

d = {"ram" : 80 ,"amit" : 90 ,"kanhaiya" : 70}
print("ram" in d)

a ={1:10}
b ={2:10}
a.update(b)
print(a)

a ={1:10}
b ={1:10}
print(a==b)'''

sta ={1:{"name":"ram","marks":80}}
print(sta)

s = "hi hi hello"
d={}
for i in s.split():
    d[i]=d.get(i,0)+1
print(d)