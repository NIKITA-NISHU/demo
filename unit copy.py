# # unit=int(input("enter units"))
# # if unit<100:
# #     print("total bill amount is no charge")
# # elif unit>=100:
# #     print("total bill amount is",unit*5)
# # elif unit<=200 and unit>=200:
# #     print("total bill amount is",unit*10)


# # unit=int(input("enter the unit:"))
# # if unit<=100:
# #     print("free")
# # elif unit >100 and unit<=200:
# #     print(unit*5,"rupeee")
# # else:
# #     print( unit*10,"rupee")

# # def my_function(fname):
# #   print(fname + " Refsnes")

# # my_function("Emil")
# # my_function("Tobias")
# # my_function("Linus")

# # def my_function(fname, lname):
# #   print(fname + " " + lname)

# # my_function("Emil", "Refsnes")

# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")

# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")

# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)

# def my_function(x):
#   return 5 * x

# print(my_function(3))
# print(my_function(5))
# print(my_function(9))

# def myfunction():
#   pass

# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)
# print(6//2-1+(7%2+3+4/2+1-2)+3**2+4*2)

# def my_function(**kid):
#     print("His last name is " + kid["lname"])
# my_function(fname = "Tobias", lname = "Refsnes")


def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)