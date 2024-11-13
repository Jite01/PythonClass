total_students = 15
passed_students = 0
failed_students = 0

print("Enter scores for", total_students, "students:")
for i in range(total_students):

  score = int(input(f"Enter score for student {i+1}: "))
           
    
if score >= 45:
        passed_students += 1
else:
        failed_students += 1
print("Number of students who passed:", passed_students)
print("Number of students who failed:", failed_students)