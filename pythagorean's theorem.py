# a = float(input("enter value of a:"))
# b = float(input("enter value of b:"))


# from math import * 


# c = round(((a**2)+(b**2))**0.5, 3)
# print("The calculated hypotenus is", c)

print("ALGORITHM TO COMPUTE THE DIFFERENT SIDES OF A TRIANGLE")

print("Note: Represent any unknown side with ",0)

opposite = float(input("enter value of the opposite side:"))
adjacent = float(input("enter value of adjacent:"))
hypotenus = float(input("enter the value of the hypotenus:"))


if opposite == 0 and adjacent == 0:
    print("you have two unknowns \ncheeck your values again") 
elif hypotenus == 0 and adjacent == 0:
    print("you have two unknowns \ncheeck your values again") 
elif opposite == 0 and hypotenus == 0:
    print("you have two unknowns \ncheeck your values again")                 
elif opposite == 0:
    opposite = round(((hypotenus**2)-(adjacent**2))**0.5, 3)
    print("The opposite side of the triangle is",opposite,"cm")
    print("i have successfully computed the opposite of the triangle")
elif adjacent ==0:
    adjacent = round(((hypotenus**2)-(opposite**2))**0.5, 3)
    print("The adjacent side of the triangle is",adjacent,"cm")
    print("i have successfully computed the adjacent of the triangle")
elif hypotenus == 0:
    hypotenus = round(((opposite**2)+(adjacent**2))**0.5, 3)
    print("The hypotenus side of the triangle is",hypotenus,"cm")
    print("i have successfully computed the hypotenus of the triangle")
   
        
