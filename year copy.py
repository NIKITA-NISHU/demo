year=int(input("enter the year"))
if year%4==0:
    print("leap year")
    if 2000%400==0:
        print("leap year")
    if 1900%400==0:
        print("leap year")
    if 2100%400==0:
        print("leap year")
else:
    print("not leap year")