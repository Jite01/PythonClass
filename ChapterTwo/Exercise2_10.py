x = int(input("Enter first integer: "))
y = int(input("Enter second integer: "))
z = int(input("Enter third integer: "))

total = x + y + z
average = total / 3
product = x * y * z
smallest = min(x, y, z)
largest = max(x, y, z)

print("Sum:", total)
print("Average:", average)
print("Product:", product)
print("Smallest:", smallest)
print("Largest:", largest)
