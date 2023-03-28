#!/usr/bin/python3
def Mortagecalc():
    # Gets the input of loan amount, Intrest and Loan terms
    loan_amount = float(input("Enter the loan amount: $"))
    interest_rate = float(input("Enter the interest rate: "))
    loan_term = int(input("Enter the loan term (in years): "))

    # Calculates the total mortage amount permonth
    monthly_rate = (interest_rate / 100) / 12 
    num_of_payments = loan_term * 12

    monthly_payment = (loan_amount * monthly_rate * (1 + monthly_rate) ** num_of_payments) / ((1 + monthly_rate) ** num_of_payments - 1)

    print("Monthly payment: $",round(monthly_payment, 2))
   

Mortagecalc()
