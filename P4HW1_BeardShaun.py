# Shaun Beaed
# 3/25/2025
# P4HW1
# Create a nested loop to collect the number of scores the user wants to enter

'''
Pseudocode

Create variable many_score (int) user input # of score
create a list (score_list)
create a for loop (for the_scores in range (many_score))
                        grade = int(input(f"Enter score # {the_scores+1}"))
                        While grade is invalid - less than 0 or greater than 100
                            print output(Score is INVALID)
                            print output(Score must be between 0 and 100)
                            grade = int(input(f"Enter score # {the_scores+1} again"))
                        score_list.append(grade)
                    print score_list see if it correct
                Get the lowest score in the list; make variable (low_score)
                Remove the lowest score fro the list
                Get the average from the list removoing the lowest score
                use average to determine the letter grade

'''

many_score = int(input("How many scores do you wan to enter? "))
score_list = []
for the_score in range(many_score):
    grade = int(input(f"Enter score #{the_score + 1}: "))
    while grade < 0 or grade >100:
        print("INVALID Score Entered")
        print("Score should be between 0 and 100")
        grade = int(input(f"Enter score #{the_score + 1} again: "))
    score_list.append(grade)
print(f"{score_list}")
print("-------------Results-------------")
print(f"{'Lowest Score ':<15}: {min(score_list)}")
score_list.remove(min(score_list))
average = sum(score_list) / len(score_list)
the_grade = ""
print(f"{'Modified List ':<15}: {score_list}")
print(f"{'Score Average ':<15}: {average}")
if average >= 90:
    the_grade = "A"
elif average >= 80:
    the_grade = "B"
elif average >= 70:
    the_grade = "C"
elif average >= 60:
    the_grade = "D"
elif average >= 50: 
    the_grade = "F"

print(f"{'Grade ':<15}: {the_grade}")
print("---------------------------------")