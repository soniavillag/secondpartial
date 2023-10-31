replit link: https://replit.com/join/wimnrkbpup-soniavillanueva

"""
Instructions:
1. Write a Python program that prompts the user to enter their birthdate (in the format: MM/DD/YYYY).
2. Calculate their zodiac sign based on their birthdate.
3. Display the determined zodiac sign to the user.
4. Make sure to handle invalid inputs gracefully (e.g., non-numeric characters or out-of-range dates).
5. Test your program with different birth dates to ensure accuracy.
"""

introduction = print("Welcome to the Zodiac Sign Calculator!")
birth_date = input("Please enter your birthdate, without the year (MM/DD): ")
if birth_date >= "12/22" and birth_date <= "01/19":
  print("Your zodiac sign is Capricorn!")

elif birth_date >= "01/20" and birth_date <= "02/18":
  print("Your zodiac sign is Aquarius!")

elif birth_date >= "02/19" and birth_date <= "03/20":
  print("Your zodiac sign is Pisces!")

elif birth_date >= "03/21" and birth_date <= "04/19":
  print("Your zodiac sign is Aries!")

elif birth_date >= "04/20" and birth_date <= "05/20":
  print("Your zodiac sign is Taurus!")

elif birth_date >= "05/21" and birth_date <= "06/20":
  print("Your zodiac sign is Gemini!")

elif birth_date >= "06/21" and birth_date <= "07/22":
  print("Your zodiac sign is Cancer!")

elif birth_date >= "07/23" and birth_date <= "08/22":
  print("Your zodiac sign is Leo!")

elif birth_date >= "08/23" and birth_date <= "09/22":
  print("Your zodiac sign is Virgo!")

elif birth_date >= "09/23" and birth_date <= "10/22":
  print("Your zodiac sign is Libra!")

elif birth_date >= "10/23" and birth_date <= "11/21":
  print("Your zodiac sign is Scorpio!")

elif birth_date >= "11/22" and birth_date <= "12/21":
  print("Your zodiac sign is Sagittarius!")

goodbye = print("Thank you for using the Zodiac Sign Calculator!")
