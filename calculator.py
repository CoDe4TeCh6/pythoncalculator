import math
import sys
print("welcome to calculator by team advtechlearn")
print("chose option: 1:add 2:subtract 3:multiply 4:divide 5:square 6:binary 7: exit")
i=int(input("Enter your choice: "))
if i>7:
    print("invalid input")
if i==1:
    print("you opted addition!")
    x=float(input("enter the first number: "))
    y=float(input("enter second number: "))
    print("your result is",x+y)

if i==2:
    print("you opted subtraction!")
    a=float(input("enter the first number"))
    b=float(input("enter the second number"))
    print("your rersult is",a-b)

if i==3:
    print("you opted multiplication")
    a=float(input("enter the first number"))
    b=float(input("enter the second number"))
    print("your rersult is",a*b)

if i==4:
    print("you opted division")
    n=float(input("enter the first number: "))
    m=float(input("enter the second number: "))
    print("your answer is",n/m)

if i==5:
    print("you opted square")
    s=float(input("enter the number: "))
    print("result=",pow(s,2))

if i==6:
    print(" you opted binary")
    d=int(input("enter your number: "))
    print("your result is",bin(d))

if i==7:
    print("you are going to exit calculator!")
    w=int(input("enter 7 again to exit: "))
    print("exit")
if i==7:
    sys.exit()

print("THANK YOU FOR USING CALCULATOR!")
