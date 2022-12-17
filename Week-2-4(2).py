#swapping two numbers with third variable
a=int(input("enter the first value:"))
b=int(input("enter the second value:"))
print("the values before swapping",a,b)
a=a+b
b=a-b
a=a-b
print("the values after swapping:",a,b)