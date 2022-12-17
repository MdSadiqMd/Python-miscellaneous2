#finding roots of an quadratic equation
import math
a=int(input("enter value of coefficient a:"))
b=int(input("enter value of coefficient b:"))
c=int(input("enter vslue of coefficient c:"))
d=(b**2)-4*a*c
if (d>0):
    r1=-b+math.sqrt(d/(2*a))
    r2=-b-math.sqrt(d/(2*a))
    print("the roots of the quadratic equations are:",r1,r2)
elif(d==0):
    r1=-b/(2*a)
    r2=-b/(2*a)
    print("the roots of the quadratic equations are:",r1,r2)
else:
    print("the roots are imaginary and does not exist")

