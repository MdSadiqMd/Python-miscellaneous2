def fact(m):
    n=1
    fact=1
    while(n<=m):
        fact=fact*n
        n=n+1
        return fact
m=int(input("enter the number:"))
print("the factorial is:",fact(m))

