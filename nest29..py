cp = int(input("enter your price"))
if cp>100000:
    print(cp*1.5)
elif cp>50000 and cp<=100000:
    print(cp*0.1)
elif cp<=50000:
    print(cp*5)