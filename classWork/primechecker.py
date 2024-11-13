def prime_checker(value):
	if value % 2 == 0:
	  print("Not prime")
	  return
          
	elif value % 3 == 0:
	  print("Not prime")
	  return

	elif value % 5 == 0:	
	  print("Not prime")

	elif value % 7 == 0:	
	  print("Not prime")


	else:
	  print ("Prime! Is your last name Optimus?")
	  


number = int(input("Enter a number..... i'll check if its prime or not: "))

if number == 2 or number == 3 or number == 5 or number == 7:
  print ("Prime! Is your last name Optimus?")
  

prime_checker(number)





