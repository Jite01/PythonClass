import random

integer1 = random.randrange(0, 100)
integer2 = random.randrange(0, 100)

total = integer1 + integer2

def guess_game()->bool:
	print('Guess the Sum:')
	guess = int(input( ))
	isCorrect = False
	if guess == total:
		isCorect = True
	return isCorrect


guess_game()
	