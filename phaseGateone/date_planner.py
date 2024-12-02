""" pseudoCode

use a match case for the first date
store the days in a list
create a function to get the date by an index pssed as an argument to the function
use a function for the second date

"""
def get_future_date(index:int)->str:
	days = ['Sunday','Monday', 'Tuesday','Wednesday','Thursday','Friday']
	return days[index]

print("Enter Today's Date-->")
today_date = int(input())

print('Enter The Number Of Days Elapsed Since Today:-->')
time_passed = int(input())

index = time_passed + today_date

match today_date:
	case 0: print(f'Today is Sunday and the future day is {get_future_date(index)}')

	case 1: print(f'Today is Monday and the future day is {get_future_date(index)}')

	case 2: print(f'Today is Tuesday and the future day is {get_future_date(index)}')

	case 3: print(f'Today is Wednesday and the future day is {get_future_date(index)}')

	case 4: print(f'Today is Thursday and the future day is {get_future_date(index)}')

	case 5: print(f'Today is Friday and the future day is {get_future_date(index)}')

	case 6: print(f'Today is Saturday and the future day is {get_future_date(index)}')
	
	case _: print("invalid stuff")





