https://replit.com/join/vcyvxvrcmn-soniavillanueva

"""
Create a program that allows the user to input the grades of a group of students.
Calculate the average grade, the highest grade, and the lowest grade. Additionally,
display how many students passed (grades greater than or equal to 60) and how
many failed.

STEPS:
1. Ask the user for the number of students DONE
2. Ask the user the grades of each student DONE 
3. Calculate and display the average grade DONE
4. Calculate and display the highest and lowest grade
5. Display how many students passed and how many didn't
"""

number_students = int(input("What is the number of students?"))
grades = []
failed = []
def students_grades():
  grade = int(input("What's the grade of the student?"))
  return grade
  grade = 0
  for _ in range(number_students):
    prev_grade = grade
    grade = students_grades()
    if grade > prev_grade:
      highest_grade = grade
    elif grade < prev_grade: 
      lowest_grade = grade
      highest_grade = prev_grade
    else: 
      lowest_grade = grade
      highest_grade = prev_grade 
    if grade < 60:
       failed.append(grade)
    grades.append(grade)
    
  average = sum(grades)/len(grades)
  number_failed = len(failed)
  numer_passed = number_students - number_failed
  
  print("The highest grade is: ", highest_grade)
  print("The lowest grade is:", lowest_grade)
  print("The average is: ", average)
  print("The number of students that have passed is: ", number_passed)
  print("The number of students that have failed is: ", number_failed)
