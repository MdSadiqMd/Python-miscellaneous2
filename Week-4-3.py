a=int(input("enter the integer:"))
count=0
while(a>=10):
    if(a%3==0):
        count+=1
        a=a//3
print(count)
