# num=int(input("enter number"))
# timing=input("enter timing")
# if num>=6 and num<=8:
#     if timing=="morning":
#         print("freshup")
#     elif num>=9 and num<=11:
#         if timing=="morning":
#             print("coding")
#     elif num==12:
#         if timing=="ofter noon":
#             print("first coding")
# elif num>=1 and num<2:
#     if timing=="ofter noon":
#         print("lounch break")
#     elif num>=2 and num<=4:
#         if timing=="ofter noon":
#             print("second coding")
# elif num>=4 and num<6:
#     if timing=="evening":
#         print("snacks break")
#     elif num>=7 and num<=8:
#         if timing=="evening":
#             print("english class")
#     elif timing=="evening":
#         if num>=8:
#             print("sleeping")
        


timing=input("enter the timing=")
num=float(input("enter the time="))
if timing=="morning":
    if num>=6 and num<=8:
        print("freshup time")
    elif num>=8.00 and num<=12.30:
        print("first coding time")
    else:
        print("morning time finish")
elif timing=="afternoon":
    if num>=12.30 and num<=2.00:
        print("lunch break")
    elif num>=2.00 and num<4.30:
        print("second coding")
elif timing=="evening":
    if num>=4.30 and num<5.00:
        print("evening exercise")
    elif num>=5.00 and num<6.00:
        print("snacks break")
    elif num>=6.00 and num<8.00:
        print("english activity")
elif timing=="night":
    if num>=8.00:
        print("dinner time")
else:
    print("nothing")
    
    


