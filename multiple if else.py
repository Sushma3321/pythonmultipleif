a=int(input("enter number"))
b=int(input("enter number"))
c=int(input("enter number"))
if a>b and b>c:
    print(a,"oldest",b,"youger",c,"youngest")
elif b>c and c>a:
    print(a,"oldest",c,"younger",b,"youngest")
elif c>a and a>b:
    print(c, "oldest",a,"younger",b,"youngest")
elif b>a and b>c:
    print(b,"oldest",a,"younger",c,"youngest")
elif c>a and a>b:
    print(a,"youngest",b,"younger",c,"oldest")
elif a>c and c>b:
    print(a,"oldest",b,"youngest",c,"younger")
else:
    print("One or more number are equal")