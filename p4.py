'''
#even odd
num = int(input("enter a number ="))
if num/2 == 0 :
    print("even")
else :
    print("odd")

#vowle consonts
character = input("enter character =")
if character in 'aeiouAEUOU':
    print("vowel")
else:
    print("consonts")'''

list =[]
for i in range (5):
    n = int(input("enter number "))
    list.append(n)
print(list)