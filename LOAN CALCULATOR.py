loan_amount =  int(input("Enter the amount of loan collected: "))
interest = int(input("Enter the interest rate on the loan: "))
interest_rate = interest/100
print("your interest_rate is ",interest_rate)
number_of_years = int(input("Enter the number of years: "))

def loan_payment(L,i,n):
    monthly_payment = L * (i * (1 + i) * n) / ((1 + i) * (n - 1))
    print("Your monthly payment will be : #",round(monthly_payment,2))

loan_payment(loan_amount,interest_rate,number_of_years)