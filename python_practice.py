
#1
x=int(input("enter a number: "))
count=0
while x>0:
    count+=1
    x//=10

if (count == 3):
    print("3 digit number")
elif(count < 3 or count>3 ):
    print("not a 3 digit number")


#2
age=int(input("Enter ur Age: "))
if(age>=18):
    print("Eligible to VOTE")
else:
    print("Not Eligible to VOTE")


#3
age=int(input("Enter ur Age: "))
if(age>=60):
    print("ur senior citizen")
else:
    print("ur NOT senior citizen")


#4
x=int(input("enter the first number: "))
y=int(input("enter the second number: "))
if (x<y):
    print(x,"is lowest number than",y)
else:
    print(y,"is lowest number than" ,x)


#5
x=int(input("enter the first number: "))
y=int(input("enter the second number: "))
if (x>y):
    print(x,"is greatest number than",y)
else:
    print(y,"is greatest number than" ,x)


#6
x=int(input("enter a number: "))
if (x>=0):
    print("Positive Number")
else:
    print("Negative Number")


#7
x=int(input("enter a number: "))
if(x==1 or x==0):
    print(x," is Neither prime nor composite number")
elif(x%2 == 0):
    print(x, "is EVEN NUMBER")
else:
    print(x, "is ODD NUMBER")


#8.1
x=int(input("Enter a number: "))
print("Entered Number is : ",end='')
if x==0:
    print("Zero")
elif x==1:
    print("One")
elif x==2:
    print("Two")
elif x==3:
    print("Three")
elif x==4:
    print("Four")
elif x==5:
    print("Five")
elif x==6:
    print("Six")
elif x==7:
    print("Seven")
elif x==8:
    print("Eight")
elif x==9:
    print("Nine")
else:
    print("Not a Digit")


#8.2
x=int(input("enter a number: "))
if(x%2==0 and x%3==0):
    print(x, " is divisible by both 2 and 3")
elif(x%2==0):
    print(x, " is only divisible by 2")
elif(x%3==0):
    print(x, " is only divisible by 3")
else:
    print(x, " is not divisible neither 2 nor 3")


#9
x=int(input("enter the first number: "))
y=int(input("enter the second number: "))
z=int(input("enter the third number: "))
print("1st number = ",x)
print("2nd number = ",y)
print("3rd number = ",z)
if (x>y and x>z):
    print(x," x is greatest number than y and z")
elif(y>x and y>z):
    print(y," y is greatest number than x and z")
else:
    print(z," z is greatest number than x and y")
