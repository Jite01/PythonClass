print('Give a number between 0 and 1000')  
user_input = int(input())


digit1 = user_input // 100
digit2 = user_input // 10 % 10
digit3 = user_input % 10

print('The sum is',digit1+ digit2 +digit3)