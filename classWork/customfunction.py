import math

def get_divide(number):
	if (number) == " ":
		print("C'mon... no input entered")
		return "C'mon... no input entered"
	
	elif type(number) not in [int, float]:
		print ("Be fr. Invalid input")
		return "Be fr. Invalid input"

	
	if number < 0:
		number = abs(number)
		if number % 5 == 0:
			result = math.sqrt(number)
			result = round(result, 2)
			print(result, 'i')
			return result
		else:
			result = number % 5
			print('-', result)
			return result


	if number % 5 == 0:
		result = math.sqrt(number)
		result = round(result, 2)
		print(result)
		return result
	else:
		result = number % 5
		print (result)
		return result

