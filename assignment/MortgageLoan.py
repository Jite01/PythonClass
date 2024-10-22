principal_amount =  float(input("Enter the principal amount: "))
annual_interest_rate = float(input("Enter the annual interest: "))
no_of_years = int(input("Enter the no of years: "))
monthly_payment = principal_amount * annual_interest_rate * (1 + annual_interest_rate) ** no_of_years / (1 + annual_interest_rate) ** no_of_years - 1
print(f"Your monthly payment is $ {monthly_payment:.2f}")