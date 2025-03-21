 # Shaun Beard

 # 3/20/2025

 # P2HW2

 # Create a program that should store the grades entered in a list.

'''
Pseudocode:

Create an empty list called 'grades' to store the grades
user input the grade for each grade to the list
Module 1 grade
Module 2 grade
Module 3 grade
Module 4 grade
Module 5 grade
Module 6 grade
 
Display the lowest grade in the list using the min() function
Display the highest grade in the list using the max() function
Display the sum of the grades using the sum() function
Calculate the average using len()function
Display the average 

'''

# Make the list
grades = []

# Input
grades.append(float(input("Enter the grade for Module 1: ")))  
grades.append(float(input("Enter the grade for Module 2: ")))  
grades.append(float(input("Enter the grade for Module 3: ")))  
grades.append(float(input("Enter the grade for Module 4: ")))  
grades.append(float(input("Enter the grade for Module 5: ")))  
grades.append(float(input("Enter the grade for Module 6: ")))  

# Calculations
lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average_grade = sum_of_grades / len(grades)

# Display 
print()
print("---------------Result---------------")
print(f"The lowest grade is: {lowest_grade}")
print(f"The highest grade is: {highest_grade}")
print(f"The sum of grades is: {sum_of_grades}")
print(f"The average grade is: {average_grade:.2f}")
print("-----------" * 4)
