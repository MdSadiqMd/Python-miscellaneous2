a=float(input("enter the score:"))
if (a>1.0):
    print("error")
elif(a<0):
    print("GRADE:A")
elif(a>=0.9):
    print("GRADE:B")
elif((a>=0.8)&(a<0.9)):
    print("GRADE:C")
elif((a<0.8)&(a>=0.7)):
    print("GRADE:D")
elif((a<0.7)&(a>=0.6)):
    print("GRADE:E")
else:
    print("fail")




