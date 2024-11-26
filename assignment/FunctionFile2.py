
def is_even(num):
    return num % 2 == 0

def is_prime_number(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def subtract(a, b):
    return abs(a - b)

def divide(a, b):
    if b == 0:
        return 0
    return a / b

def factor_of(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count

def is_square(num):
    return num ** 0.5 % 1 == 0

def is_palindrome(num):
    original_num = num
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return original_num == reversed_num

def factorial_of(num):
    if num == 0:
        return 1
    return num * factorial_of(num - 1)

def square_of(num):
    return num * num