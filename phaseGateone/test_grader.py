import os
from datetime import datetime
import random


answerlist = []
actual_answers = []
score = 0

for i in range(1,11):
	current_time = datetime.now()
	num1 = random.randrange(1, 20)+ 19
	num2 = random.randrange(1, 20)
	print(f'Question{i}:','Subtract',num1, 'from', num2 )
	answer = int(input())
	answerlist.append(answer)
	actual_answers.append(num1 - num2)
	os.system('cls')

for i in range(0,10):
	if answerlist[i] == actual_answers[i]:
		score += 1
	
print ('Your score is',score,'out of 10\n')
print('your time taken was', )

	


