import random

integer1 = random in range(0, 100)
integer2 = random in range(0, 100)

total = integer1 + integer2

def guess_game()->bool:
	print('Guess the Sum:')
	guess = input(int( ))
	isCorrect = False
	if guess == total:
		isCorect = True
	return isCorrect


guess_game()
	