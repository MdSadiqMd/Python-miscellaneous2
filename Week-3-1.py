#whether the studentis eligible to sit in exam or not
a=int(input("enter number of working days:"))
b=int(input("enter number of days absent:"))
c=(b/a)*100
if (c>75):
    print("the student is eligible to dit in exam hall")
else:
    print("the student is not eligible to sit in exam hall")