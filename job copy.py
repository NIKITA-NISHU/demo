employee=input("enter your gender")
age=int(input("enter youe age"))
if employee=="female":
    print("she will work only in urban areas")
elif employee=="male":
    if age>=20:
        if age<=40:
            print("he may work in any where")
    if age>=40:
        if age<=60:
            print("he will work in urban areas only")
        else:
            print("ERROR")
else:
    print("ERROR")
    
    

    
    