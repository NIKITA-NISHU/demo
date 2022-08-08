status=input("enter the status")
age=int(input("enter the age"))
if status=="married":
    if age>=20:
        if age<=40:
            print("you have to do hard work")
    else:
        print("you have to do not hard work")    
    if age>=40:
        if age<=60:
            print("you have to do normal work")
    else:
        print("you have to do not normal work")
    if age>60:
        print("you should take rest")
    else:
        print("you should not take rest")
elif status=="unmarried":
    if age>=15:
        if age<=25:
            print("you should do study")
    else:
        print("you should not do study")
    if age>25:
        print("you should marry and do job")
    else:
        print("you should not marry and do not job")