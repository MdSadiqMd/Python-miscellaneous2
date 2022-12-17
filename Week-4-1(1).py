rows=int(input("enter number of rows:"))
for i in range(0,rows):
    for j in range(0,i+1):
        print("*",end=" ")
    print()
for j in range(rows+1,0,-1):
    for j in range(0,i-1):
        print("* ",end="")
    print()
