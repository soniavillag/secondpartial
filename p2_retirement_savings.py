https://replit.com/join/dujobwxipt-soniavillanueva

"""
Create a program that helps people calculate how much they need to save
monthly for retirement. Ask the user for their current age, the age at which they
plan to retire, and the desired retirement amount. Then, calculate how much they
should save monthly, considering an expected annual investment return. Use the
formula:
➔ PMT is the required monthly payment.
➔ FV is the desired retirement amount.
➔ r is the monthly interest rate (annual return divided by 12, expressed as a
decimal).
➔ n is the number of monthly payments in retirement (years of retirement
multiplied by 12).
➔ t is the number of years until retirement.
Display the monthly payment required to reach the retirement goal.

STEPS 
1. Enter the current age. 
2. Enter the age you want to retire.
3. Enter your desired retirement amount.
4. Calculate how much they should save monthly, considering an expected annual investment return.
"""

current_age = int(input("Please enter your current age: "))
retirement_age = int(input("Please enter the age at which you would like to retire: "))
retirement_amount = int(input("Now enter your desired retirement amount "))

monthly_savings = (retirement_amount - (current_age * 12)) / ((retirement_age - current_age) * 12)

print ("You would need to save", monthly_savings, "per month to reach your goal")
