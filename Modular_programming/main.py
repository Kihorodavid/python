# import modulator module
import operators
import others
import trig
# build a better calculator
# x=others.cube(3)
# y=operators.add(9,3)
# print(x)
# print(y)
operator=input("Enter operator :")
if operator == "cube":
    num = eval(input("Enter number :"))
    x=others.cube(num)
    print(x)
elif operator=="sin":
    angle= eval(input("Enter angle in degrees :"))
    x=trig.sin(angle)
    print(x)

elif operator=="tan":
    angle= eval(input("Enter angle in degrees :"))
    x=trig.tan(angle)
    print(x)

elif operator=="cos":
    angle= eval(input("Enter angle in degrees :"))
    x=trig.cos(angle)
    print(x)
else:
    num1=eval(input("Enter number :"))
    num2=eval(input("Enter number :"))


    if operator=="+":
        x=operators.add(num1,num2)
        print(x)
    if operator=="-":
        x=operators.subtract(num1,num2)
        print(x)
    if operator== "x" or operator=="X" or operator=="*":
        x=operators.multiply(num1,num2)
        print(x)
    if operator=="/":
        x=operators.divide(num1,num2)
        print(x)
        
