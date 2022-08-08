# unit=int(input("enter the unit"))
# bill=0
# if unit<100:
#     print("no charge")
# elif unit>100:
#     print(unit*5)
# elif unit>200 and unit<200:
#     print(unit*10)
    

unit=int(input("enter the number units"))
if unit<=100:
    print("no charge",unit)
if unit>100 and unit<200:
    bill=unit-100
    print(bill*5)
if unit>200:
    bill=unit-200
    print(bill*10+100*5)
