# star in angle
rows = int(input("enter number of rows:"))
for i in range (1, rows + 1):
      print(" " *(rows-1),end = " ") 
      print(" * " * i )

#opse in angle
rows= int(input("enter number of rows :"))
for i in range(rows , 0 , -1):
    for j in range(i):
        print("*", end=" ")
    print()
