p2_multiple_discounts.py

"""
Write a program that allows the user to enter the price of a product and its category
(A, B, or C). Then, apply discounts based on the category and the number of units
purchased. For example:
Category A: 10% discount.
Category B: 5% discount.
Category C: 2% discount.
Furthermore, if the user buys more than 10 units, an additional 5% discount is
applied. Display the final price after all discounts.
"""

product = float(input("Please enter the price of your product: "))
category = input("Now enter the category of your product, either A, B, C: ")
units = int(input("Now please enter the number of units that were purchased: "))

discount = 0
additional_discount = 0

if category == "A":
  discount = 10

elif category == "B":
  discount = 5

elif category == "C":
  discount = 2

else:
  if unit == 10: 
    additional_discount = +5

final_price = product - (product * discount / 100) + (product * additional_discount / 100)

  
print ("This is your final price after the discounts: ", final_price)
