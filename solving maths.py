# print("This program computes the solutions to a quadratic equation")

# import math

# def main():

#     a = float(input("Enter the value of a:"))
#     b = float(input("Enter the value of b:"))
#     c = float(input("Enter the value of c:"))

#     discRoot = math.sqrt((b**b)- 4 *a * c)

#     sol1 = (-b + discRoot)/(2 * a)
#     sol2 = (-b - discRoot)/(2 * a)

#     print("The solutions to the quadratic equation are:",sol1,  sol2)


# main()



# print("solve this problem below")

# x = (3 * 10)//(3 + (10%3))
# print("find x ?")
# print("The solution of x is:",x)
import math

# x = 4 * pi * (r**2)
# print("The solution of x is",x)


# for i in range(10):
#     print(i*i)

# ans = 0
# for i in range (1, 11) :
#     ans = ans + i*i
#     print (i)
#     print (ans)

#PROGRAM TO COMPUTE THE AREA AND THE VOLUME OF A SPHERE
radius = float(input("Enter the radius:"))
pi = 3.142
volume_of_sphere = (4/3)* pi * (radius**3)
area_of_sphere = 4 * pi * (radius *2)

print("The volume of the sphere is:",volume_of_sphere,"cm cb")
print("The are of the sphere is:",area_of_sphere,"cm sq")


#PROGRAM TO COMPUTE THE MOLECULAR WEIGHT OF CARBOHYDRATE
# hydr = int(input("Enter the no of hydrogen atoms: "))
# oxyg = int(input("Enter the no of oxygen atoms: "))
# carb = int(input("Enter the no of carbon atoms: "))

# MW_of_carbohydrate = ((hydr*1.00794) + (oxyg*12.0107) * (carb*15.9994))
# print ("The molecular weight of carbohydrate is:",round(MW_of_carbohydrate,-2),"grams per mole")


#PROGRAM TO COMPUTE THE DISTANCE AWAY FROM A LIGHTNING STRIKE IN MILES
# time_of_strike = int(input("Enter the time of strike:"))
# speed_of_sound = 1100

# distance_in_ft = speed_of_sound * time_of_strike
# distance_in_miles = distance_in_ft/ 5280

# print("The distance away from the strike in feet is:",distance_in_ft,"feet")
# print("The distance away from the strike in miles is:",distance_in_miles,"miles")


#PROGRAM TO COMPUTE THE COST OF A SHIPPING ORDER
# Amount_of_coffee = int(input("Enter the amount of coffee sold in pound:"))
# cost_of_shipping = (0.86 * Amount_of_coffee) + 1.50

# print("The cost of shipping is",cost_of_shipping,"dollars")


#PROGRAM TO COMPUTE THE SLOPE OF A LINE AND DISTANCE BETWEEN TWO POINTS

# first_x1 = float(input("Enter the first value of x:"))
# second_x2 = float(input("Enter the second value of x:"))
# first_y1 = float(input("Enter the first value of y:"))
# second_y2 = float(input("Enter the second value of y:"))

# slope_of_line = (second_y2 - first_y1)/(second_x2 - first_x1)
# distance_of_points = ((second_x2 - first_x1)**2 + (second_y2 - first_y1)**2)**0.5

# print("The slope of the line graph is:",slope_of_line)
# print("The distance between the two points is:",distance_of_points)


#PROGRAM TO FIGURE OUT THE DATE OF EASTER BASED ON THE YEAR INPUT

# choice_year = int(input("Enter the year:"))
# #Note: epact is a special formula to compute the easter day based on the year given
# C = choice_year//100
# epact =  (8 + (C//4)- C + ((80 + 13)//25) + 11 * (choice_year%19))%30
# print("The day of easter is:",epact)


#PROGRAM TO COMPUTE THE AREA OF A TRIANGLE
# first_length = int(input("Enter the first side:"))
# second_length = int(input("Enter the second side:"))
# third_length = int(input("Enter the third side:"))

# average_length = (first_length + second_length + third_length)/3

# Area = (average_length * (average_length - first_length) * (average_length - second_length) * (average_length - third_length)) ** 0.5

# print("The Area of the traingle is:",Area)


#PROGRAM TO COMPUTE THE SUM OF NATURAL NUMBERS

# natural_number = int(input("Enter the value of n:"))
# sum = 0
# sum_of_cube = 0
# for i in range(natural_number+1):
#     sum += i
#     sum_of_cube += i**3
#     # print(sum)
#     if i == natural_number:
#         print("The sum of first",natural_number,"natural number is:",sum)    
#         print("The sum of the cubes of the first",natural_number,"natural number is:",sum_of_cube)
 

#PROGRAM TO COMPUTE A LIST OF NUMBERS ENTERES BY USERS

# numbers_to_compute = int(input("How many numbers do you want to compute: "))
# summed_number = 0
# for number in range (numbers_to_compute):
#     entered_numbers = int(input("Enter your number here:"))
#     summed_number += entered_numbers
# # TO COMPUTE THE AVERAGE OF THE NUMBERS ENTERED 
#     mean_of_number = summed_number/numbers_to_compute   
#     if number == numbers_to_compute -1:
#         print("The sum of the ",numbers_to_compute,"numbers you entered is ",summed_number)
#         print("The average of the ",numbers_to_compute,"numbers you entered is ",round(mean_of_number,2))

    



  
