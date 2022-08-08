num1=int(input("enter your number"))
num2=int(input("enter your number"))
num3=int(input("enter your number"))
if num1>num2 and num1>num3:
    if num2>num3:
        print(num2, "is second maximum")
    else:
        print(num3, "is second maximum")
else:
    if num2>num1:
        print(num2,"is second maximum")
    else:
        print(num1,"is second ,maximum")



    
