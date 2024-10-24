number=int(input('Enter three digit: '))

firstint = number //100
secondint = number % 10

palindrome = firstint / secondint

if palindrome == 1:
	print(number, 'is a palindrome')
else:
	print(number, 'is not a palindrome')