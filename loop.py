# for x in "banana":
#     print(x)

# _list = [1,2,3,"banana",5]   

# for element in _list:
#     print(element)

#     for letter in str(element):
#         print(letter)

# name = input("what is your name?")
# count = 0

# for characters in name:
#     count +=1
# print("The total character in your name is",count)    


#Exhaustive enumeration
# password = 2001

# for i in range(9999):
#     print("testing", i)
#     if password == i:
#         print ("your password is", i)
#         break
    
possible_result = [111,222,333,444,555,666,777,888,999]

for i in range(100,999):
    total_sum = 3*i
    if total_sum in possible_result and i%10 in possible_result:
        print(total_sum)
        break

     
       
