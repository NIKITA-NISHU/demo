floor=int(input("enter the floor"))
girls=int(input("enter the girls"))
bed=int(input("enter the bed"))
room="room=4"
c=bed-girls
d=girls-bed
if floor==1:
    print(room)
    if bed>girls:
        print(c,"bed is empty")
    elif girls>bed:
        print(d,"girls are much")
    else:
        print("bed")
elif floor==2:
    print(room)
    if bed>girls:
        print(c,"bed is empty")
    elif girls>bed:
        print(d,"girls are much")
    else:
        print("bed")
elif floor==3:
    print(room)
    if bed>girls:
        print(c,"bed is empty")
    elif girls-bed:
        print(d,"girls are much")
    else:
        print("bed")
elif floor==4:
    print(room)
    if bed>girls:
        print(c,"bed is empty")
    elif girls-bed:
        print(d,"girls are much")
    else:
        print("bed")
else:
    print("floor")
    

