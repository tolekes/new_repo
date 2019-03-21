# def greet(person):
#     print("Good morning",person)
#     print("i am excited to see you")
# (greet("tolu"))



# names = ["tolu","bola","samuel","Atiku"]
# ages = [24,26,19,90]

# def say_hello(name,age):
#     computer_age = 20

#     if computer_age < age:
#         print("e kaabo", name)
#     else:
#         print("kaabo", name)    
    
# for x,y in zip(names,ages):  
#     say_hello(x,y)        

# class_A = [34,34,56,78]
# class_B = [87,34,23,22]
# class_C = [23,22,33,44]

# def sum(A,B,C):
#     total = A + B + C
#     print(total)
# for x,y,z in zip(class_A, class_B, class_C) :
#     sum(x,y,z) 
   

# class_A = [34,34,56,78]
# class_B = 34

# def sum_of_class(_list):

#     sum = 0
#     if isinstance(_list, list):
#         for item in _list:
#             sum += item
#         print("the sum of ", _list,"is",sum)  
#     else:
#         print(type(_list),"is not a list")   

# sum_of_class(class_B)   


# products = {
#      "beans" : 100,
#      "rice" : 200,
#      "garri" : 400,
#      "ogbono" : 300
# }

# cars = {
#     "jaguar" : 1000,
#     "honda" : 2000,
#     "camry" : 3000
# }

# def sum_of_product(my_dict):
#     sum = 0
#     for price in my_dict:
#         sum += my_dict[price]
#     print("The total sum of is: ",sum)
    
# sum_of_product(cars)


# print(1,2,3,4, sep ="/", end ="?")


#program that gives us the biggest no betwween two values

# def max_val(x,y):
#     if x>y:
#         return x
#     elif y>x:
#         return y
#     else:
#         return "No greater value"

# print(max_val(44,44))



#PROGRAM TO COMPARE LENGTHS OF NAMES
# first_name = input("what is your first name: ")
# second_name = input("what is your second name: ")

# def name_length(x,y):
#     if int(len(x)) > int(len(y)):
#         return "first name is the longest name"
#     elif int(len(x)) < int(len(y)):
#         return "second name is the longest name"
#     else:
#         return "your names have thesame length"

# print(name_length(first_name,second_name))


#PROGRAM TO COMPUTE FACTORIALS

# def factorial(n):
#     fact = 1
#     while n >= 1:
#         fact = fact * n
#         n = n - 1 
#     return fact

# print(factorial(5))



#PROGRAM TO COMPUTE THE MOLECULAR WEIGHT OF CARBOHYDRATE
# hydr = int(input("Enter the no of hydrogen atoms: "))
# oxyg = int(input("Enter the no of oxygen atoms: "))
# carb = int(input("Enter the no of carbon atoms: "))

# def molecule(x,y,z):

#     MW_of_carbohydrate = ((x*1.00794) + (y*12.0107) * (z*15.9994))
#     return "The molecular weight of carbohydrate is:",round(MW_of_carbohydrate,-2),"grams per mole"

# print(molecule(hydr,oxyg,carb))




#PROGRAM TO EVALUATE A CHAOTIC FUNCTION

# value= float(input("Enter the value of x between 0 and 1: "))
# ite = int(input("Enter the number of iteration: "))

# def chaos(x,n):
#     for i in range(n):
#       x = 3.9 * x * (1-x)
#       return x

# print(chaos(value,ite))   


def frac(num1,den1,num2,den2):
    firstnum = num1 * den2
    secondnum = num2 * den1
    total_num = firstnum + secondnum
    total_den = den1 * den2
   
    
    
    for i in reversed(range(1,10)):
        if total_num %i == 0 and total_den%i == 0:
            total_num = total_num// i
            total_den = total_den//i 
    
    print(str(total_num)+"/"+str(total_den))

frac(21,6,34,5) 
