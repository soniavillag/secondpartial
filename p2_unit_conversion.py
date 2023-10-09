https://replit.com/join/vqrzwoigrm-soniavillanueva

"""
Create a program that allows the user to convert between different units of
measurement, such as miles to kilometers, liters to gallons, or Fahrenheit to Celsius.
The program should prompt the user for the quantity and unit of origin and the unit of
destination, then perform the conversion.
"""

quantity = int(input("Enter the quantity: "))
unit_origin = input("Enter the unit of origin (miles, liters, fahrenheit, etc.): ")
unit_destination = input("Enter the unit of destination (kilometers, gallons, etc.): ")

for i in range(quantity): 
  if unit_origin == "miles":
    if unit_destination == "kilometers":
      print(f"{quantity} miles is {quantity * 1.609} kilometers")
    elif unit_destination == "liters": 
      print(f"{quantity} miles is {quantity * 1.609} liters")
      
  elif unit_origin == "liters":
    print(f"{quantity} liters is {quantity * 0.454545} gallons")
    
  elif unit_origin == "fahrenheit":
    if unit_destination == "celsius": 
      print(f"{quantity} fahrenheit {quantity * (5/4) - 32} celsius")
    elif unit_destination == "kelvin": 
      print(f"{quantity} fahrenheit {quantity * (5/4) - 32} kelvin")
    elif unit_origin == "kelvin": 
      print(f"{quantity} kelvin is {quantity * (5/4) - 32} fahrenheit")
    elif unit_origin == "celsius": 
      print(f"{quantity} celsius is {quantity * (5/4) - 32} kelvin")
      
  elif unit_origin == "kilometers" and unit_destination == "miles": 
    print(f"{quantity} kilometers is {quantity * 1.609} miles")
    
  elif unit_origin == "gallons" and unit_destination == "liters": 
    print(f"{quantity} gallons is {quantity * 3.3} liters")

  elif unit_origin == "celsius" and unit_destination == "fahrenheit": 
    print(f"{quantity} celsius is {quantity * (9/4) + 32} fahrenheit") 

  elif unit_origin == "kelvin" and unit_destination == "fahrenheit": 
    print(f"{quantity} kelvin is {quantity * (9/4) + 32} fahrenheit")
    
  elif unit_origin == "celsius" and unit_destination == "kelvin": 
    print(f"{quantity} celsius is {quantity * (9/4) + 32} kelvin")
    
  elif unit_origin == "kelvin" and unit_destination == "celsius": 
    print(f"{quantity} kelvin is {quantity * (9/4) + 32} celsius")

else: 
  print("this is an invalid input")
