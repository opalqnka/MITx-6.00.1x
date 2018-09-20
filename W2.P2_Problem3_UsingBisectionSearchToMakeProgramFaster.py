"""
The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

To recap the problem: we are searching for the smallest monthly payment such that we can pay off the entire balance within a year. 
What is a reasonable lower bound for this payment value? $0 is the obvious anwer, but you can do better than that. If there was no 
interest, the debt can be paid off by monthly payments of one-twelfth of the original balance, so we must pay at least this much every 
month. One-twelfth of the original balance is a good lower bound.

What is a good upper bound? Imagine that instead of paying monthly, we paid off the entire balance at the end of the year. 
What we ultimately pay must be greater than what we would've paid in monthly installments, because the interest was compounded 
on the balance we didn't pay off each month. So a good upper bound for the monthly payment would be one-twelfth of the balance, 
after having its interest compounded monthly for an entire year.

In short:

Monthly interest rate = (Annual interest rate) / 12.0
Monthly payment lower bound = Balance / 12
Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

Write a program that uses these bounds and bisection search (for more info check out the Wikipedia page on bisection search) to 
find the smallest monthly payment to the cent (no more multiples of $10) such that we can pay off the debt within a year. 
Try it out with large inputs, and notice how fast it is (try the same large inputs in your solution to Problem 2 to compare!). 
Produce the same return value as you did in Problem 2.
"""

#monthly_interest_rate does not change
monthly_interest_rate = annualInterestRate / 12.0

#save value of initial balance to do resets
balance_saved = balance

#define epsilon up to 2 significant figures
epsilon = 0.01

monthly_payment_lower = balance / 12
monthly_payment_upper = (balance * (1 + monthly_interest_rate)**12) / 12.0
monthly_payment_actual = (monthly_payment_lower + monthly_payment_upper ) / 2.0

while (abs(balance) >= epsilon):
    balance = balance_saved
    for i in range(12):
        monthly_unpaid_balance = balance - monthly_payment_actual
        balance = monthly_unpaid_balance + monthly_interest_rate * monthly_unpaid_balance
        
    if balance >= 0:
        monthly_payment_lower = monthly_payment_actual    
    else:
        monthly_payment_upper = monthly_payment_actual
        
    monthly_payment_actual = (monthly_payment_lower + monthly_payment_upper ) / 2.0
        
print("Lowest Payment: ", str(round(monthly_payment_actual,2)))
