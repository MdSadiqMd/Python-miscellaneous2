def LCM(a,b):
    LCMmultiple=LCMmultiple+b
    if(LCMmultiple%a==0)and(LCMmultiple%b==0):
        return LCMmultiple
    else:
        LCM(a,b)
        return LCMmultiple
LCMmultiple=0
a=int(input("enter first number:"))
b=int(input("enter second number:"))
if(a>b):
    LCM=LCM(a,b)
else:
    LCM=LCM(a,b)
print("LCM is:",LCM)






