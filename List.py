# # months is a list used as a lookup table
# months = [ " Jan" , " Feb " , "Mar " , "Apr " , " May " , " Jun" ,
# " Jul " , " Aug" , " Sep " , " Oct " , " Nov " , "Dec " ]
# n = int ( input ( "Enter a month number ( 1-12) : " ) )
# print ( " The " + str(n) +"th month is " + months [n-1] + " . " )


# shopping_cart = ["apple", "coca cola", "soap", "chicken"]

# print(shopping_cart[0])
# print("there are " + str(len(shopping_cart))+ " elements in the list")

# shopping_cart.append("barbecue")
# print(shopping_cart)
# print("there are " + str(len(shopping_cart))+ " elements in the list")

# shopping_cart.insert(3,"mayonnaise")
# print(shopping_cart)
# print("there are " + str(len(shopping_cart))+ " elements in the list")

# duplicate_cart = shopping_cart.copy()
# print ("duplicate", duplicate_cart)

# shopping_cart.clear()
# print ("new shopping list", shopping_cart)

# duplicate_cart.pop(4)
# print ("duplicate", duplicate_cart)

# duplicate_cart.insert(4,"chicken")
# print ("duplicate", duplicate_cart)

# duplicate_cart.reverse()
# print (" duplicate", duplicate_cart)

# duplicate_cart.sort()
# print (" duplicate", duplicate_cart)

# age = 25
# while age < 30:
  
#     your_name = input("Enter your first name:")

#     list_name = list(your_name)
#     reverse_name = list_name.reverse()
#     new_name = "".join(list_name)
#     print(new_name)
#     age += 1



     #while loop and Listing 
# while True:
  
#     your_name = input("Enter your first name:")

#     list_name = list(your_name)
#     reverse_name = list_name.reverse()
#     new_name = "".join(list_name)
#     if your_name == new_name:
#         print("This is a palindrome")
#     else:
#         print("This is not a palindrome")    
#     if your_name == "end":
#         break
#     print(new_name)
    
shopping_cart  = ["apple","orange", "coca cola", "chicken","pork","ham","palony"] 
print(shopping_cart[::])  
print(shopping_cart[1:4])
shopping_cart[::2] = [1,2,3,4]
print(shopping_cart)

