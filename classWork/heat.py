total_students = 15
pass_counter = 0
fail_counter = 0

print("Enter scores for", total_students, "students:")

for i in range(total_students):

 score = float(input(f"Enter the scores for Student{i+1}: ")) 

	
if score >= 45:
        pass_counter += 1
else:
        fail_counter += 1
print("Number of students who passed:", pass_counter)
print("Number of students who failed:", fail_counter)