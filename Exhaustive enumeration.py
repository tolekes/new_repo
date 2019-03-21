possible_result = [111,222,333,444,555,666,777,888,999]  #lookup table for the results

for initial_number in range(100,999):    #the range is between 100 and 999 because the numbers being added are 3 figured
    total_sum_of_numbers = 3*initial_number # i multiplied by 3 because the three no added are thesame
    if total_sum_of_numbers in possible_result and str(initial_number%10) in str(total_sum_of_numbers):  
            #the line above provides 2 conditions 
            # in the 2nd condition, %10 returns the last digit and searched for it in the numbers added.
        print(initial_number)      
        print(total_sum_of_numbers)
         