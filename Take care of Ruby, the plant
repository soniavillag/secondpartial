replit link: https://replit.com/join/bxrqovxqrf-soniavillanueva

"""
STEPS: 
1. You must create program to take care of Ruby, a plant.
2. You must be careful with the environmental temperature (in Celcius).
2.1. Between 20 and 12 = good condition, below 20 = to be inside, above 25 = inside and fan on.
3. You must be careful with the percentage of humidity in the air.
3.1. Less than 20 = water it, greater or equal to 20, and less than and equal to 22 = suitable.
4. You must take into consideration the day of the week.
4.1. Ruby should be watered on Tuesdays, Thursdays and Saturdays. 
"""

introduction = input("Hello!, lets take care or Ruby, the plant, shall we?: ")

if introduction == "yes":
  print("Okay, let's go!")

elif introduction == "no":
  print("Let's do it anyways!")

else:
  print("Please enter a valid answer.")

day = input("What day is it today?: ")
if day == "Tuesday" or day == "Thursday" or day == "Saturday":
  print("You shall water Ruby today.")

elif day == "Monday" or day == "Wednesday" or day == "Friday" or day == "Sunday":
  print("You shall not water Ruby today")

temperature = int(input("What's the temperature in Celcius right now?: "))

if temperature >= 20 and temperature <= 25:
  print("Perfect!, then Ruby is in good conditions.")

elif temperature < 20:
  print("You need to bring Ruby inside the house, it's too cold!")

elif temperature > 25:
  print("You need to bring Ruby inside the house and turn the fan on, it's too hot!")

humidity = int(input("What's the current humidity of the air?: "))

if humidity < 20:
  print("You should water Ruby, I bet she's thirsty.")

if humidity >= 20 and humidity <= 22:
  print("That's a suitable humidity for Ruby, she's okay.")

elif humidity > 22 and (day == "Monday" or day == "Wednesday" or day == "Friday" or day == "Sunday"):
  print("It's not necessary to water Ruby, she's ok.")

elif humidity > 22 and (day == "Tuesday" or day == "Thursday" or day == "Saturday"):
  print("It's necessary to water Ruby.")

goodbye = input("Was this useful for you?: ")

if goodbye == "yes":
  print("That's good!, I'm glad.")

elif goodbye == "no":
  print("That's a shame :O")

else:
  print("Please enter a valid answer.")
