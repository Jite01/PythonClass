days = int(input("Enter the number of days the book is late: "))

if days <= 5:
   fine = days * 0.50
   print(f"Fine amount: {fine}")
elif days <= 10:
   fine = days * 1
   print(f"Fine amount: {fine}")
elif days <= 30:
   fine = days * 5
   print(f"Fine amount: {fine}")
else:
   print("Your membership has been cancelled due to long delay")