costprice=int(input("enter the cost price="))
percentage=costprice*100
if costprice>100000:
    print("tax is",costprice*15)
if costprice>50000 and costprice<=100000:
    print("tax is",costprice*10)
if costprice<=50000:
    print("tax is",costprice*5)