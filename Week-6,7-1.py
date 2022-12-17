name=input("enter the name of the student:")
rollno=int(input("enter roll number of the student:"))
m1,m2,m3,m4,m5=map(int(input("enter marks of five subjects:")).split(" "))
sum=m1+m2+m3+m4+m5
avg=sum/5
print("individual scores of %s with roll.no %d are %d,%d,%d,%d,%d total attained is %d and average is %2f",(name,rollno,m1,m2,m3,m4,m5,sum,avg))