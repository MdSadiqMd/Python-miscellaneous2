#leap year or not
year=int(input("enter the value of year:"))
if((year%400==0)&(year%100==0)):
    print(year,"is a leap year")
elif((year%100!=0)&(year%4==0)):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")