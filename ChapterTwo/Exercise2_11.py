number = int(input("Enter a five-digit number: "))
digit1 = number // 10000
pendigit1 = (number // 1000)

digit2 = pendigit1 % 10
pendigit2 = (number // 100)
digit3 = pendigit2 % 10
pendigit3 = (number // 10)
digit4 = pendigit3 % 10
digit5 = number % 10

print(digit1, digit2, digit3, digit4, digit5)
