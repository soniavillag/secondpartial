https://replit.com/join/ihviixsbic-soniavillanueva

"""
Create a program that calculates the calories burned during physical activity. Ask the
user to input their weight in kilograms, the duration in minutes, and the type of
activity (running, swimming, cycling, etc.). Use specific formulas for each activity and
display the total calories burned.

STEPS:
1. Ask the user to input their weight in kg.
2. Ask the user to input the duration of their exercise in minutes.
3. Ask the user to input their activity type.
4. Calculate the total calories burned and display them.
"""

weight = int(input("Please enter your current weight on kilograms: "))
duration = int(input("Please enter the duration of your exercises in minutes: "))
activity = input("What type of activity do you do? (cardio, strength or both): ")

calories_burned = 0
if activity == "cardio":
  calories_burned1 = weight * (0.03 * duration)
  print("You burned", calories_burned1, "calories during cardio")

elif activity == "strenght":
  calories_burned2 = weight * (0.04 * duration)
  print("You burned", calories_burned2, "calories during strenght")

elif activity == "both":
  calories_burned3 = weight * (0.07 * duration)
  print("You burned", calories_burned3, "calories by doing both")
