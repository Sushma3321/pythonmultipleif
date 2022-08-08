num=int(input("enter number"))
timing=input("enter timing")
if num>=6  and num<=8 and timing=="morning":
    print("freshup")
elif num>=9 and num<=11 and timing=="morning":
    print("coding")
elif num==12 and timing=="morning":
    print("first coding")
elif num>12 and num<2  and timing=="ofter noon":
    print("lounch break")
elif num>=2 and num<4 and timing=="ofter noon":
    print("second coding")
elif num>=4 and num<6 and timing=="evening":
    print("snacks break")
elif num>=6 and num<8 and timing=="evening":
    print("english class")
elif num>=8 and timing=="night":
    print("sleeping")

