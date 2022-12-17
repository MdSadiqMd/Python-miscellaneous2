#integer to binary
n=int(input("enter an integer:"))
while(n<0):
    n = int(input("enter an integer:"))
if(n==999):
    quit()
c=0
sum=0
while(n!=0):
    rem=n%2
    sum=rem*(10**c)+sum
    n=n//2
    c=c+1
print("the binary number is",sum)