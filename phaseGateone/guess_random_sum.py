import random


def guess_game(guess: int)->bool:
	isCorrect = False

	if guess != total:
		print(isCorrect)
		print('Guess the Sum:')
		guess = int(input())

	if guess == total:
		isCorrect = True
	print(isCorrect)
	return isCorrect

	
integer1 = random.randrange(0, 100)
integer2 = random.randrange(0, 100)

total = integer1 + integer2

print('Guess the Sum:')
guess = int(input())

guess_game(guess)

	