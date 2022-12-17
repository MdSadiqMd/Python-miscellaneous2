n=int(input("enter the number"))
sum=0
i=1
while(n<100):
    if(n%2!=0):
        sum=sum+n
        n=n+1
    else:
        n=n+1
        continue
print("the sum of odd numbers is",sum)