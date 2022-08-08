phy=int(input("enter the marks="))
chem=int(input("enter the marks="))
bio=int(input("enter the marks="))
math=int(input("enter the marks="))
com=int(input("enter the marks="))
total=phy+chem+bio+math+com
per=total*100/500
print("total",total)
print("percentage=",per)
if per>=90:
    print("grade A")
elif per>=80 and per<=90:
    print("grade B")
elif per>=70 and per<=80:
    print("grade C")
elif per>=60 and per<=70:
    print("grade D")
elif per>=40 and per<=60:
    print("grade E")
elif per<40:
    print("grade F")