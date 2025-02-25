# dictionary
students = {1276:"ken Burns", 5428:"homer Simpson", 6437:"Sonic Hedge"}
print(students[1276])

# Get the key from the user
student_id = int(input("give me a Student ID: "))
print(f"The student with ID {student_id} is {students[student_id]}")

# add a new key value pair to dictionary
students[1020] = ("Shaun Weard")
print(students)