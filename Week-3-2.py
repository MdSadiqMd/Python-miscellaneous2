a=int(input("cost of the bike:"))
b=(15/100)*a
c=(10/100)*a
d=(5/100)*a
if(a>100000):
    print("the bike will get into 15% tax of price:",b)
elif((a>50000)&(a<100000)):
    print("the bike will get into 10% tax of price:",c)
else:
    print("the bike will get into 55 tax of price:",d)