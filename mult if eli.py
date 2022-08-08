exam=input("enter exam")
result=input("enter result")
if exam=="online":
    if result=="pass":
        print("pass you can eligible for interview")
    else:
        print("sorry you can try again")
elif exam=="introduction":
    if result=="pass":
      print("then you can eligible for algebra interview")
    else:
        print("sorry try again") 
elif exam=="algebra":
    if result=="pass":
        print("then you can eligible for cultural fit round ")
    else:
        print("sorry you can try again")
elif exam=="cultural fit":
    if result=="pass":
        print("then you can join in navgurukul")
    else:
        print("sorry you can try again")

