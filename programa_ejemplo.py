# Este programa sirve para
def programa():
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))
    num3=float(input("Enter third number: "))
    if (num1>=num2) and (num1>=num3):
        x=num1
    else:
        if (num2>=num1) and (num2>=num3):
            x=num2
        else:
            x=num3
    print ("",x)

programa()
