#amstrong or not
import math
a=int(input("enter a number"))
sum=0
num=a
l=0
while(num>0):
    l=l+1
    num=int(num/10)
    num=a
    while(num>0):
        r=num%10
        sum=sum+pow(r,l)
        num=int(num/10)
if (a==sum):
    print(a,"is a amstrong number")
else:
    print(a,"is not a amstrong number")