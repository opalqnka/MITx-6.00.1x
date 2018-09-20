"""
Now write a program that calculates the minimum fixed monthly payment needed in order pay off 
a credit card balance within 12 months. By a fixed monthly payment, we mean a single number 
which does not change each month, but instead is a constant amount that will be paid each month.

Assume that the interest is compounded monthly according to the balance at the end of the month 
(after the payment for that month is made). The monthly payment must be a multiple of $10 and is 
the same for all months. Notice that it is possible for the balance to become negative using this 
payment scheme, which is okay. A summary of the required math is found below:


Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance) 

"""
#to be defined by grader
#balance = 3329
#annualInterestRate = 0.2

#does not depend on our calculations
monthly_interest_rate = annualInterestRate / 12.0
#start with lowest payment
min_monthly_payment = 10
#save the balance value
balance_saved = balance
done = False

while done != True:
    balance = balance_saved
    for i in range(1,13):        
        monthly_unpaid_balance = balance - min_monthly_payment
        balance = monthly_unpaid_balance + monthly_interest_rate * monthly_unpaid_balance
    if balance > 0:
            min_monthly_payment += 10
    else:
        done = True
            
print("Lowest Payment: ", min_monthly_payment)
